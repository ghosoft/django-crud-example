# Generated by Django 3.1.4 on 2022-06-29 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
