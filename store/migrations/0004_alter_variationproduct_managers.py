# Generated by Django 5.0.4 on 2024-04-15 22:02

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variationproduct'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='variationproduct',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
