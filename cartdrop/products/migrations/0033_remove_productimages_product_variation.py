# Generated by Django 3.2.5 on 2021-08-16 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0032_auto_20210816_2018"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productimages",
            name="product_variation",
        ),
    ]
