# Generated by Django 3.2.5 on 2021-08-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0028_auto_20210816_1858"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimages",
            name="product_variation",
            field=models.ManyToManyField(
                blank=True, related_name="images", to="products.ProductVariation"
            ),
        ),
    ]
