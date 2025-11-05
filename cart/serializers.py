from rest_framework import serializers

from cart.models import CartItem


class CreateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']