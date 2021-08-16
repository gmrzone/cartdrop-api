# Generated by Django 3.2.5 on 2021-08-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0022_remove_productwarranty_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="overall_rating",
            field=models.DecimalField(
                blank=True, decimal_places=1, default=0.0, max_digits=1
            ),
        ),
    ]
