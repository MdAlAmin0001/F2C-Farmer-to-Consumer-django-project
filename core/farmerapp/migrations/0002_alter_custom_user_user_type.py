# Generated by Django 5.0 on 2024-01-02 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='user_type',
            field=models.CharField(choices=[('farmer', 'Farmer'), ('user', 'User'), ('agent', 'Agent'), ('admin', 'Admin')], max_length=120),
        ),
    ]
