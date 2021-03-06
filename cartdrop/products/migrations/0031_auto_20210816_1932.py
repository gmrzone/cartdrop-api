# Generated by Django 3.2.5 on 2021-08-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0030_alter_productimages_product_variation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productimages",
            name="product_variation",
        ),
        migrations.AddField(
            model_name="productvariation",
            name="images",
            field=models.ManyToManyField(
                blank=True, related_name="for_variations", to="products.ProductImages"
            ),
        ),
    ]
