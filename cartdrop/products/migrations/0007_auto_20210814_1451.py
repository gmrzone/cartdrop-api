# Generated by Django 3.2.5 on 2021-08-14 14:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_auto_20210814_1205"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductWarranty",
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
                ("type", models.CharField(max_length=100)),
                ("summary", models.CharField(max_length=200)),
                ("covered", models.TextField(blank=True, max_length=500)),
                ("not_covered", models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="RefrigeratorType",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SpeakerType",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="specification",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="product",
                to="products.productspecification",
            ),
        ),
        migrations.CreateModel(
            name="ProductSpeakersFeatures",
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
                ("power_output", models.CharField(max_length=20)),
                ("frequency_response", models.CharField(max_length=100)),
                ("has_blootooth", models.BooleanField(default=False)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.speakertype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductRefrigeratorFeature",
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
                ("capacity", models.CharField(max_length=100)),
                (
                    "star_rating",
                    models.PositiveIntegerField(
                        default=3,
                        validators=[django.core.validators.MaxValueValidator(5)],
                    ),
                ),
                ("compressor_type", models.CharField(max_length=100)),
                ("stabilizer_required", models.BooleanField(default=False)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.refrigeratortype",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productspecification",
            name="refrigerator",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.productrefrigeratorfeature",
            ),
        ),
        migrations.AddField(
            model_name="productspecification",
            name="speaker",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.productspeakersfeatures",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="warranty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.productwarranty",
            ),
        ),
    ]
