# Generated by Django 3.2.5 on 2021-08-14 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_auto_20210814_1451"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productmobilefeatures",
            name="variant",
        ),
        migrations.DeleteModel(
            name="MobileVariants",
        ),
    ]
