# Generated by Django 4.0.1 on 2022-01-25 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnc_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnc_Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'CNC Sub-Category',
                'verbose_name_plural': 'CNC Subcategories',
            },
        ),
        migrations.AddField(
            model_name='cnc_product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cnc_products.cnc_cat'),
        ),
    ]
