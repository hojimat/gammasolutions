# Generated by Django 4.0.4 on 2022-05-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_alter_customer_address_alter_customer_telegram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='originCity',
            field=models.CharField(default='New York', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='destinationState',
            field=models.CharField(default='CA', max_length=2),
        ),
    ]