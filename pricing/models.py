from django.db import models

from lib.common_model import BaseModel


class PricingRule(BaseModel):
    RULE_TYPES = [
        ('fixed_discount', 'Fixed Discount'),
        ('percent_discount', 'Percentage Discount'),
    ]

    rule_type = models.CharField(max_length=20, choices=RULE_TYPES)
    condition_value = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Minimum cart total or quantity to apply the rule"
    )
    discount_amount = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Amount or percentage to discount"
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rule_type} - {self.discount_amount}"