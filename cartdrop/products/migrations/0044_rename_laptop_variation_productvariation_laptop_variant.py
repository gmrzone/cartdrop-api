# Generated by Django 3.2.5 on 2021-08-24 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0043_auto_20210824_0619"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productvariation",
            old_name="laptop_variation",
            new_name="laptop_variant",
        ),
    ]
