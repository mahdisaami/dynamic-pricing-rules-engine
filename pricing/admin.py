from django.contrib import admin

from pricing.models import PricingRule


@admin.register(PricingRule)
class PricingRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_type', 'condition_value', 'discount_amount', 'active', 'created_at')
    list_filter = ('rule_type', 'active')
    search_fields = ('rule_type',)
    ordering = ('rule_type',)