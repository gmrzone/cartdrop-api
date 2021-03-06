# Generated by Django 3.2.5 on 2021-08-26 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0049_productvariation_tv_variant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productvariation",
            name="color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.productcolor",
            ),
        ),
    ]
