# Generated by Django 4.0.4 on 2022-05-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0010_order_completed_order_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokerdocument',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brokerdocument',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driverdocument',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driverdocument',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderdocument',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderdocument',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
