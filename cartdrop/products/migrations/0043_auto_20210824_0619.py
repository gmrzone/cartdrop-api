# Generated by Django 3.2.5 on 2021-08-24 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0042_laptopvariant"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productlaptopfeatures",
            name="ram",
        ),
        migrations.RemoveField(
            model_name="productlaptopfeatures",
            name="storage",
        ),
        migrations.AddField(
            model_name="productvariation",
            name="laptop_variation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.laptopvariant",
            ),
        ),
    ]
