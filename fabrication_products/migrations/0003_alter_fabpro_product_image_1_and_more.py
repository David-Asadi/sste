# Generated by Django 4.0.1 on 2022-01-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrication_products', '0002_fabpro_product_image_1_fabpro_product_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabpro',
            name='product_image_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fabpro',
            name='product_image_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fabpro',
            name='product_image_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fabpro',
            name='product_image_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fabpro',
            name='product_image_5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
