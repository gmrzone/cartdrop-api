# Generated by Django 3.2.5 on 2021-08-15 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0015_auto_20210815_1334"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productrefrigeratorfeature",
            old_name="star_rating",
            new_name="energy_rating",
        ),
        migrations.RemoveField(
            model_name="productmobilefeatures",
            name="variant",
        ),
        migrations.AddField(
            model_name="productmobilefeatures",
            name="series",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productseries",
            ),
        ),
        migrations.AddField(
            model_name="productvariation",
            name="variant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.mobilevariant",
            ),
        ),
    ]
