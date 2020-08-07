from django.db import models
import uuid

from filters.models import ProductFilter


class PageModel(models.Model):

    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=255)
    seo_description = models.CharField(max_length=255)
    text = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Catalog(PageModel):

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'catalogs'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=str
    )
    image = models.FileField(upload_to='catalog/%Y/%m/%d/')
    product_filter = models.ManyToManyField(
        ProductFilter,
        related_name='catalog',
    )


class Product(PageModel):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'products'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.SET_NULL,
        null=True,
    )


class ProductVariable(models.Model):
    class Meta:
        verbose_name = 'Product variable'
        verbose_name_plural = 'product variables'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    var_name = models.CharField(max_length=255)
    var_value = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
