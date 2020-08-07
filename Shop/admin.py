from django.contrib import admin

from Shop.models import (
    ProductVariable,
    Product,
    Catalog,
)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass


class ProductVariableStackInline(admin.StackedInline):
    model = ProductVariable


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    inlines = (ProductVariableStackInline, )
