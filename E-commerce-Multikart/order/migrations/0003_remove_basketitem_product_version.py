# Generated by Django 5.0 on 2024-03-04 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_transaction_code_remove_basketitem_basket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='product_version',
        ),
    ]
