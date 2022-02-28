# Generated by Django 4.0.2 on 2022-02-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_useraddress_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdropuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. set this to false this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
