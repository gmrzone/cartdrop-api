# Generated by Django 3.2.5 on 2021-08-14 20:08

import django.db.models.deletion
from django.db import migrations, models

import cartdrop.core.utils


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20210814_0833"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productsubcategory",
            name="photo",
        ),
        migrations.CreateModel(
            name="SubcategoryImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to=cartdrop.core.utils.category_images),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subcategory_images",
                        to="core.productsubcategory",
                    ),
                ),
            ],
        ),
    ]