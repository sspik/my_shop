from django.db import models
import uuid


class PageModel(models.Model):

    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

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

    def __str__(self):
        return self.name


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
    properties = models.JSONField(null=True, blank=True)
    options = models.JSONField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.catalog.name}'
