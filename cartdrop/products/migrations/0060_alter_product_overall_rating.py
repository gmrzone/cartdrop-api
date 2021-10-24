# Generated by Django 3.2.5 on 2021-10-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0059_productimages_placeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='overall_rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2),
        ),
    ]