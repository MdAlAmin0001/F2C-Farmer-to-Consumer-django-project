# Generated by Django 5.0 on 2023-12-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_addjob_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjob_model',
            name='Job_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]