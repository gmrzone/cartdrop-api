# Generated by Django 3.2.5 on 2021-08-07 11:57

import django.db.models.deletion
from django.db import migrations, models

import cartdrop.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Slugable",
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
                ("slug", models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "slugable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.slugable",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField()),
                ("name", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(upload_to=cartdrop.core.utils.category_images),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.slugable", models.Model),
        ),
        migrations.CreateModel(
            name="ProductSubcategory",
            fields=[
                (
                    "slugable_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.slugable",
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField()),
                ("name", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(upload_to=cartdrop.core.utils.subcategory_images),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subcategories",
                        to="core.productcategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.slugable", models.Model),
        ),
    ]