from django.contrib import admin
from basket.models import CardPosition, Card


class CardPositionsInlineAdmin(admin.StackedInline):
    model = CardPosition


@admin.register(Card)
class BasketAdmin(admin.ModelAdmin):
    inlines = (CardPositionsInlineAdmin,)
