from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=255, verbose_name='модель')
    launch_date = models.DateField(verbose_name='дата выхода')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.model})'
