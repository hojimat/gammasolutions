# Generated by Django 4.0.4 on 2022-05-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0018_trailer_height_trailer_length_trailer_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='weight',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
