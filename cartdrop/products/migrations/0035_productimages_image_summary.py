# Generated by Django 3.2.5 on 2021-08-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0034_auto_20210816_2046"),
    ]

    operations = [
        migrations.AddField(
            model_name="productimages",
            name="image_summary",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
