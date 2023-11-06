# Generated by Django 4.2.5 on 2023-11-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_remove_subcategory_category_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(to='product.subcategory')),
            ],
        ),
    ]