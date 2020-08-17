import os
import uuid

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings


RECOMMEND = 'R'
NEW = 'N'
HIT = 'H'


PRODUCT_STATUS = (
    (RECOMMEND, 'Recommend'),
    (NEW, 'New'),
    (HIT, 'Hit'),
)


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
    image = models.FileField(upload_to='upload/product/%Y/%m/%d/')

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
    image = models.ImageField(upload_to='upload/product/%Y/%m/%d/', null=True, blank=True)
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.SET_NULL,
        null=True,
    )
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    product_status = models.CharField(
        max_length=1,
        choices=PRODUCT_STATUS,
        null=True,
        blank=True
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.catalog.name}'


@receiver(pre_delete, sender=Product)
def delete_product_with_image(instance, **kwargs):
    instance.image.delete()


@receiver(pre_save, sender=Product)
def delete_changed_image(instance, **kwargs):
    current_product = Product.objects.get(id=instance.id)
    if current_product.image and \
            current_product.image != instance.image:
        if os.path.isfile(current_product.image.path):
            current_product.image.delete()
