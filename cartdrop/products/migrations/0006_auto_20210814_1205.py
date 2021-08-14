# Generated by Django 3.2.5 on 2021-08-14 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0005_auto_20210814_1159"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productlaptopfeatures",
            name="processor",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="productlaptopfeatures",
            name="ram",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="productlaptopfeatures",
            name="series",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.productseries"
            ),
        ),
        migrations.AlterField(
            model_name="productmobilefeatures",
            name="ram",
            field=models.CharField(max_length=100),
        ),
    ]