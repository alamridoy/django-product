# Generated by Django 4.2.5 on 2023-11-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_products_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category_name',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ManyToManyField(to='product.category'),
        ),
    ]
