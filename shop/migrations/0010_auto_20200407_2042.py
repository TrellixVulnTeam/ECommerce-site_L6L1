# Generated by Django 3.0.2 on 2020-04-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200407_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]