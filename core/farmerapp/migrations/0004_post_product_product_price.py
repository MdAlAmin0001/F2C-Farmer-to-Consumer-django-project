# Generated by Django 5.0 on 2024-01-03 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0003_rename_post_description_post_product_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_product',
            name='Product_price',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
