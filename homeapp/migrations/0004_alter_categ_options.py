# Generated by Django 3.2.6 on 2021-08-10 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]