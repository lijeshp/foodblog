# Generated by Django 3.2.6 on 2021-08-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0006_product_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
