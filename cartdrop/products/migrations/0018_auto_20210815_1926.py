# Generated by Django 3.2.5 on 2021-08-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0017_auto_20210815_1904"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="PID",
        ),
        migrations.RemoveField(
            model_name="product",
            name="available_colors",
        ),
        migrations.AddField(
            model_name="productvariation",
            name="PID",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="A Unique Product Identification Number",
                max_length=50,
            ),
        ),
    ]