# Generated by Django 3.2.6 on 2021-08-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_alter_categ_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
