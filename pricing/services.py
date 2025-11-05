from products.models import Product
from pricing.models import PricingRule

class PricingService:
    def __init__(self, cart_items):
        self.cart_items = cart_items
        self.rules = PricingRule.objects.filter(active=True)

    def calculate_final_price(self):
        subtotal = self._calculate_subtotal()
        total_discount = 0

        for rule in self.rules:
            if subtotal >= rule.condition_value:
                total_discount += self._apply_rule(subtotal, rule)

        final_price = max(subtotal - total_discount, 0)
        return {"subtotal": subtotal, "discount": total_discount, "final_price": final_price}

    def _calculate_subtotal(self):
        subtotal = 0
        for item in self.cart_items:
            product = Product.objects.get(id=item["product_id"])
            subtotal += product.price * item["quantity"]
        return subtotal

    def _apply_rule(self, subtotal, rule):
        if rule.rule_type == "fixed_discount":
            return rule.discount_amount
        elif rule.rule_type == "percent_discount":
            return subtotal * (rule.discount_amount / 100)
        return 0
