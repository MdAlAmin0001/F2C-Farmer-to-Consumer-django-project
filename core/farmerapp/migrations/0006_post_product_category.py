# Generated by Django 5.0 on 2024-01-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0005_post_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_product',
            name='category',
            field=models.CharField(choices=[('none', 'None'), ('vegetables', 'Vegetables'), ('grocery', 'Grocery'), ('fruits', 'Fruits'), ('clothes', 'Clothes')], default='none', max_length=20),
        ),
    ]