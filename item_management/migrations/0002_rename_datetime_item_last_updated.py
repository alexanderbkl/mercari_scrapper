# Generated by Django 3.2.9 on 2021-11-26 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='datetime',
            new_name='last_updated',
        ),
    ]