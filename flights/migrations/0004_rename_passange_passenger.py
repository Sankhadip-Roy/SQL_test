# Generated by Django 4.1.7 on 2023-03-14 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passange'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passange',
            new_name='Passenger',
        ),
    ]
