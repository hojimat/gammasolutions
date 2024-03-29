# Generated by Django 4.0.4 on 2022-05-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0021_order_height_order_length_order_weight_order_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default='2022-01-13 08:00'),
        ),
        migrations.AlterField(
            model_name='order',
            name='destination_market',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='origin_market',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='pickup_date',
            field=models.DateTimeField(default='2022-01-13 08:00'),
        ),
    ]
