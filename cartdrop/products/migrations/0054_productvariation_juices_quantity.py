# Generated by Django 3.2.5 on 2021-08-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0053_productvariation_refrigerator_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariation',
            name='juices_quantity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]