# Generated by Django 5.0 on 2024-01-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0004_post_product_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_product',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
