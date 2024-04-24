# Generated by Django 5.0.4 on 2024-04-24 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_chains', '0003_remove_grocerychain_products'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grocery_chains.grocerychain', verbose_name='производитель'),
            preserve_default=False,
        ),
    ]
