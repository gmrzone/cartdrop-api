# Generated by Django 3.2.5 on 2021-08-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0050_alter_productvariation_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productspeakersfeatures",
            name="frequency_response",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="productspeakersfeatures",
            name="power_output",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
