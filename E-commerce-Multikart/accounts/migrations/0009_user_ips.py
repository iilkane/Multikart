# Generated by Django 5.0 on 2024-03-02 15:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ips',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.GenericIPAddressField(), blank=True, null=True, size=None),
        ),
    ]
