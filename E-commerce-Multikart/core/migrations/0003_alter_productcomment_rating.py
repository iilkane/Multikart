# Generated by Django 5.0 on 2024-04-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_productcomment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
