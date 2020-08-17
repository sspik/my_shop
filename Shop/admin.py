from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db.models import JSONField
from Shop.models import (
    Product,
    Catalog,
)


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
