# Generated by Django 4.0.1 on 2022-01-27 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plastic_products', '0003_alter_plast_cat_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plast_cat',
            options={'verbose_name': 'Plastic Sub-Category', 'verbose_name_plural': 'Plastic Subcategories'},
        ),
    ]
