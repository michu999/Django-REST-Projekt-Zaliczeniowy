from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Uzytkownik(AbstractUser):
    ROLE_CHOICES = [
        ('TECHNICIAN', _('Technik farmaceuta')),
        ('BACHELOR', _('Farmaceuta z licencjatem')),
        ('MASTER', _('Magister farmacji')),
    ]
    rola = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='TECHNICIAN',
        verbose_name=_('Rola użytkownika')
    )

class Lek(models.Model):
    CATEGORY_CHOICES = [
        ('OTC', _('Bez recepty')),
        ('PRESCRIPTION', _('Na receptę')),
        ('RPKW', _('Rpw - ścisłe kontrolowane')),
    ]

    nazwa = models.CharField(max_length=100, verbose_name=_('Nazwa leku'))
    kategoria = models.CharField(max_length=12, choices=CATEGORY_CHOICES, verbose_name=_('Kategoria leku'))

    def __str__(self):
        return self.nazwa
