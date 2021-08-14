# Generated by Django 3.2.5 on 2021-08-14 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210814_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='productmobilefeatures',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.mobilevariant'),
        ),
    ]
