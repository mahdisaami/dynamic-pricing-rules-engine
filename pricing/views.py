from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart, CartItem
from cart.serializers import CreateCartSerializer
from pricing.services import PricingService
from products.models import Product


class PriceCalculatorView(APIView):
    def post(self, request):
        cart_items = request.data.get("items", [])
        if not cart_items:
            return Response({"error": "No items provided"}, status=status.HTTP_400_BAD_REQUEST)

        service = PricingService(cart_items)
        result = service.calculate_final_price()

        return Response(result, status=status.HTTP_200_OK)

