# Generated by Django 5.0.4 on 2024-04-24 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_chains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerychain',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grocery_chains.grocerychain', verbose_name='поставщик'),
        ),
    ]
