# Generated by Django 4.0.4 on 2022-05-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0010_driver_city_alter_driver_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='Palo Alto', max_length=30),
        ),
    ]