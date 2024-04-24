from django.db import models
from django.utils.translation import gettext_lazy as _

from products.models import Product


class GroceryChain(models.Model):

    class STRUCTURE(models.TextChoices):
        factory = 'factory', _('Завод')
        retail = 'retail', _('Розничная сеть')
        individual_entrepreneur = 'individual_entrepreneur', _('Индивидуальный предприниматель')

    name = models.CharField(max_length=100, unique=True, verbose_name='название')
    type_structure = models.CharField(max_length=50, choices=STRUCTURE.choices, verbose_name='структура')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукты')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='задолженность')
    date_created = models.DateField(auto_now_add=True, verbose_name='дата создания')

    email = models.EmailField(max_length=100, unique=True, verbose_name='электронная почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=100, verbose_name='номер дома')

    class Meta:
        verbose_name = 'торговое звено'
        verbose_name_plural = 'торговые звенья'

    def __str__(self):
        return self.name
