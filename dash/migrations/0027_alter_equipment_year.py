# Generated by Django 4.0.4 on 2022-05-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0026_alter_document_broker_alter_document_driver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='year',
            field=models.IntegerField(blank=True, default=2000),
        ),
    ]
