# Generated by Django 5.0.4 on 2024-04-15 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('store', '0004_alter_variationproduct_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ManyToManyField(blank=True, to='store.variationproduct'),
        ),
    ]
