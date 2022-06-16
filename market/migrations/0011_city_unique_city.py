# Generated by Django 4.0.4 on 2022-06-15 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_alter_city_options'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='city',
            constraint=models.UniqueConstraint(fields=('name', 'state'), name='unique_city'),
        ),
    ]