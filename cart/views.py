from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CreateCartSerializer
from products.models import Product


class MakeCartItem(APIView):
    def post(self, request):
        serializer = CreateCartSerializer(data=request.data)
        if serializer.is_valid():
            cart_item = serializer.save()
            product = cart_item.product
            quantity = cart_item.quantityk
            try:
                cart = Cart.objects.create()
                cart.items.add(cart_item)
                subtotal = cart.subtotal()
                data = {"Cart_id": cart.id, "Product": product.name, "Quantity": quantity, "Subtotal": subtotal}
                return Response(data, status=status.HTTP_201_CREATED)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)