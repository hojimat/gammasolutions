# Generated by Django 4.0.4 on 2022-05-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0020_alter_order_destination_market_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='height',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='length',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='weight',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='width',
            field=models.FloatField(blank=True, default=0),
        ),
    ]