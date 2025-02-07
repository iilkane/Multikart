# Generated by Django 5.0 on 2023-12-19 17:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.CharField(max_length=100, verbose_name='flat')),
                ('adress', models.TextField(max_length=300, verbose_name='adress')),
                ('zip_code', models.CharField(max_length=10, verbose_name='zip_code')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('region', models.CharField(max_length=100, verbose_name='region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShippingAdress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
