# Generated by Django 4.0.4 on 2022-05-10 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_alter_brokerdocument_expiry_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brokerdocument',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='driverdocument',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='orderdocument',
            old_name='name',
            new_name='title',
        ),
    ]
