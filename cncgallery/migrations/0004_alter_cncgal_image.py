# Generated by Django 4.0.1 on 2022-01-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cncgallery', '0003_remove_cncgal_img_title_cncgal_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cncgal',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]