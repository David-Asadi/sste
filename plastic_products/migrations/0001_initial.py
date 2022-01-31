# Generated by Django 4.0.1 on 2022-01-25 04:06

import ckeditor.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plastic_Product',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('used_for', models.CharField(max_length=200, null=True)),
                ('material', models.CharField(max_length=200, null=True)),
                ('thumbnail_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('product_image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image_4', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image_5', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Plastic Product item',
                'verbose_name_plural': 'Plastic Products',
            },
        ),
    ]
