# Generated by Django 3.2.5 on 2021-08-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_alter_productvariation_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariation',
            old_name='PID',
            new_name='pid',
        ),
    ]