# Generated by Django 3.1.4 on 2021-02-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20210201_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='emailid',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
