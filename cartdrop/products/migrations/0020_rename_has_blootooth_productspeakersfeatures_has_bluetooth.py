# Generated by Django 3.2.5 on 2021-08-15 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0019_auto_20210815_1937"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productspeakersfeatures",
            old_name="has_blootooth",
            new_name="has_bluetooth",
        ),
    ]
