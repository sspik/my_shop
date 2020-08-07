from django.contrib import admin
from filters.models import ProductFilter, ProductFilterValue


class ProductFilterValueStackInLine(admin.StackedInline):
    model = ProductFilterValue


@admin.register(ProductFilter)
class ProductFilterAdmin(admin.ModelAdmin):
    inlines = (ProductFilterValueStackInLine, )
