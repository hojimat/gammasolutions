# Generated by Django 4.0.4 on 2022-05-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_alter_driver_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Skip')], default='M', max_length=10),
        ),
    ]
