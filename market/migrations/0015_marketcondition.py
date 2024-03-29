# Generated by Django 4.0.4 on 2022-06-16 18:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0014_city_metro_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('temperature', models.FloatField(default=0)),
                ('precipitation', models.CharField(blank=True, choices=[('SUN', 'Sunny'), ('WND', 'Windy'), ('CLD', 'Cloudy'), ('RNY', 'Rainy'), ('SNW', 'Snowy'), ('STM', 'Stormy'), ('FOG', 'Foggy')], default='SUN', max_length=10)),
                ('l2t_van', models.FloatField(blank=True, default=1.0)),
                ('mci_van', models.FloatField(blank=True, default=1.0)),
                ('rate_van', models.FloatField(blank=True, default=1.0)),
                ('l2t_reefer', models.FloatField(blank=True, default=1.0)),
                ('mci_reefer', models.FloatField(blank=True, default=1.0)),
                ('rate_reefer', models.FloatField(blank=True, default=1.0)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='conditions', to='market.city')),
            ],
        ),
    ]
