# Generated by Django 4.0.4 on 2022-05-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0019_truck_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination_market',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='origin_market',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='truck',
            name='model',
            field=models.CharField(default='', max_length=50),
        ),
    ]
