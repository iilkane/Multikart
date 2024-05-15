# Generated by Django 5.0 on 2024-02-03 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='products.size'),
        ),
    ]
