# Generated by Django 4.0.4 on 2022-06-15 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0042_alter_order_destination_city_alter_order_origin_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='destination_market',
        ),
        migrations.RemoveField(
            model_name='order',
            name='origin_market',
        ),
    ]