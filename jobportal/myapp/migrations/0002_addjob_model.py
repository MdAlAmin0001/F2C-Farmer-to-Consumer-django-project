# Generated by Django 5.0 on 2023-12-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addjob_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]
