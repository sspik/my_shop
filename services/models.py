from django.db import models
from Shop.models import PageModel
from autoslug import AutoSlugField


class Service(PageModel):

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'services'

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(null=True, blank=True, upload_to='services')
    enable = models.BooleanField(default=False)

    def __str__(self):
        return self.title
