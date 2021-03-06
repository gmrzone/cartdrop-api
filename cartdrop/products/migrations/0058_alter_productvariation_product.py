# Generated by Django 3.2.5 on 2021-08-29 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0057_rename_pid_productvariation_pid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productvariation",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="variations",
                to="products.product",
            ),
        ),
    ]
