# Generated by Django 3.1.7 on 2021-04-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210403_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='coef',
            field=models.FloatField(default=1.1),
        ),
    ]