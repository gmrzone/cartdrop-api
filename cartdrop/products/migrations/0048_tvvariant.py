# Generated by Django 3.2.5 on 2021-08-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0047_auto_20210826_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_size', models.CharField(max_length=100)),
            ],
        ),
    ]