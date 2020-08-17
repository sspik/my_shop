from django.contrib.auth.models import User
from django.db import models

from Shop.models import Product


class Card(models.Model):

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'cards'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        return self.card_positions.all().values('price')


class CardPosition(models.Model):

    class Meta:
        verbose_name = 'Card position'
        verbose_name_plural = 'card positions'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card_positions')

    @property
    def price(self):
        return self.product.price * self.count

