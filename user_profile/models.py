from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

PERSON = 'P'
COMPANY = 'C'
user_type_choices = [
    (PERSON, 'Person'),
    (COMPANY, 'Company'),
]


class Requisites(models.Model):
    class Meta:
        verbose_name = 'Requisites'
        verbose_name_plural = 'requisites'

    legal_address = models.TextField()
    postal_address = models.TextField()
    inn = models.IntegerField()
    kpp = models.IntegerField()


class Profile(models.Model):

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'profiles'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    user_type = models.CharField(
        max_length=1,
        choices=user_type_choices,
        default=PERSON
    )
    photo = models.FileField(
        null=True,
        upload_to='photos',
        blank=True
    )
    address = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )
    requisites = models.ForeignKey(
        Requisites,
        on_delete=models.CASCADE,
        null=True
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
