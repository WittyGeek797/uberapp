# Generated by Django 2.0.7 on 2018-07-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uberapi', '0002_auto_20180729_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='availablity',
            field=models.BooleanField(default=True),
        ),
    ]
