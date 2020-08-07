from django.db import models
import uuid

NUMBER = 'N'
STRING = 'S'
BOOLEAN = 'B'

product_variable_choices = [
    (NUMBER, 'Number'),
    (STRING, 'String'),
    (BOOLEAN, 'Boolean'),
]


class ProductFilter(models.Model):
    class Meta:
        verbose_name = 'Product filter'
        verbose_name_plural = 'product filter'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=255)
    value_type = models.CharField(
        max_length=1,
        choices=product_variable_choices,
        default=STRING
    )


class ProductFilterValue(models.Model):
    class Meta:
        verbose_name = 'Product variable value'
        verbose_name_plural = 'product variable values'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    value = models.CharField(max_length=255)
    filter_name = models.ForeignKey(
        ProductFilter,
        related_name='product_filter_value',
        on_delete=models.SET_NULL,
        null=True
    )
