from django.views.generic import TemplateView, FormView, View, RedirectView
from django.core.urlresolvers import reverse_lazy
from tienda.cart import Cart
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tienda.views.cart import CartEntrySerializer, CartEntry
from rest_framework import permissions

SESSION_KEY = 'TIENDA_CHECKOUT_KEY'

class Checkout(object):
    request = None

    def __init__(self, checkout_storage):
        self.checkout_storage = checkout_storage

    def start(self, cart):
        checkout_storage = self.checkout_storage
        checkout_storage[u'cart'] = cart.session_storage #TODO shallow copy?
        checkout_storage[u'address'] = None
        checkout_storage[u'shipping_method'] = None
        checkout_storage[u'payment_method'] = None

    @property
    def cart_entries(self):
        cart = Cart(self.checkout_storage[u'cart'])
        entries = []
        for p, q in cart.storage.iteritems():
            entries.append(CartEntry(p.pk, q, p.name, p.price,
                p.get_first_category().pk, p.images.first(),
                 p.calculate_discount(Checkout.request.discounts)))
        return entries
    
    @property
    def shipping_address(self):
        return self.checkout_storage[u'address']

    @shipping_address.setter
    def shipping_address(self, address):
        print "SETTING ADDRESS", address
        self.checkout_storage[u'address'] = address

    @property
    def shipping_method(self):
        return self.checkout_storage[u'shipping_method']

    @shipping_method.setter
    def shipping_method(self, shipping):
        self.checkout_storage[u'shipping_method'] = shipping

    @property
    def shipping_price(self):
        return self.checkout_storage[u'shipping_price']

    @shipping_price.setter
    def shipping_price(self, price):
        self.checkout_storage[u'shipping_price'] = price

    @property
    def payment_method(self):
        return self.checkout_storage[u'payment_method']

    @payment_method.setter
    def set_payment_method(self, payment):
        self.checkout_storage[u'payment_method'] = payment

    def create_order(self):
        # TODO preconditions
        pass
        # TODO delete storage

class CheckoutSerializer(serializers.Serializer):
    shipping_address = serializers.CharField(allow_null=True)
    shipping_method = serializers.IntegerField()
    payment_method = serializers.IntegerField()
    cart_entries = CartEntrySerializer(many=True, read_only=True)

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        #instance.shipping_price = # TODO
        if 'payment_method' in self.validated_data:
            instance.payment_method = self.validated_data.get('payment_method')

        if 'shipping_address' in self.validated_data:
            instance.shipping_address = self.validated_data.get('shipping_address')

        if 'shipping_method' in self.validated_data:
            instance.shipping_method = self.validated_data.get('shipping_method')
        return instance


class CheckoutDetailRESTView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        Checkout.request = request
        if SESSION_KEY not in self.request.session:
            self.request.session[SESSION_KEY] = {}

        checkout = Checkout(self.request.session[SESSION_KEY])
        serializer = CheckoutSerializer(checkout)
        return Response(serializer.data)

    def put(self, request):
        Checkout.request = request
        if SESSION_KEY not in self.request.session:
            self.request.session[SESSION_KEY] = {}
        checkout = Checkout(self.request.session[SESSION_KEY])
        # TODO shipping_price
        serializer = CheckoutSerializer(checkout, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InitCheckoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        #TODO redirect t o login/register and dont start chechout
        cart = Cart(self.request.cart)
        if SESSION_KEY not in self.request.session:
            self.request.session[SESSION_KEY] = {}
        checkout = Checkout(self.request.session[SESSION_KEY])
        checkout.start(cart)

        url = '/checkout/'
        return url

class CheckoutView(TemplateView):
    template_name = ''
