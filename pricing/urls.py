from django.urls import path
from .views import PriceCalculatorView

urlpatterns = [
    path("calculate/", PriceCalculatorView.as_view(), name="price-calculate"),

]
