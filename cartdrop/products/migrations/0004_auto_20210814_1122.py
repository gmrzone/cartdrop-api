# Generated by Django 3.2.5 on 2021-08-14 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_auto_20210814_1001"),
    ]

    operations = [
        migrations.CreateModel(
            name="OperatingSystem",
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
                ("slug", models.SlugField(blank=True, max_length=100)),
                ("name", models.CharField(db_index=True, max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ScreenType",
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
        migrations.AddField(
            model_name="product",
            name="warranty",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="weight",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name="productspecification",
            name="launched_date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="PID",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="A Unique Product Identification Number",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="productmobilefeatures",
            name="display_size",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="ProductTelivisionFeatures",
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
                ("display_size", models.CharField(max_length=100)),
                ("is_3d", models.BooleanField(default=False)),
                ("is_curved", models.BooleanField(default=False)),
                ("has_wify", models.BooleanField(default=True)),
                ("usb_count", models.PositiveIntegerField(default=0)),
                (
                    "screen_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.screentype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductLaptopFeatures",
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
                ("display_size", models.CharField(max_length=100)),
                ("resolution", models.CharField(max_length=100)),
                ("battery_backup", models.CharField(max_length=100)),
                ("touchscreen", models.BooleanField(default=True)),
                ("storage", models.CharField(max_length=100)),
                (
                    "display_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.displaytype",
                    ),
                ),
                (
                    "os",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.operatingsystem",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="productmobilefeatures",
            name="os",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.operatingsystem",
            ),
        ),
        migrations.AddField(
            model_name="productspecification",
            name="laptop",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.productlaptopfeatures",
            ),
        ),
        migrations.AddField(
            model_name="productspecification",
            name="tv",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products.producttelivisionfeatures",
            ),
        ),
    ]