# Generated by Django 3.1.7 on 2021-04-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210403_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='begin_heating',
            field=models.DateField(default='2020-10-15'),
        ),
    ]