# Generated by Django 3.1.4 on 2021-02-02 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20210201_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagetable',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='imagetable',
            name='quantity',
        ),
    ]