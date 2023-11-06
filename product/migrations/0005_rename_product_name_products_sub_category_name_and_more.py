# Generated by Django 4.2.5 on 2023-11-01 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_category_products_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_name',
            new_name='sub_category_name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
    ]