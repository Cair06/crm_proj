# Generated by Django 4.1.1 on 2022-09-06 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='manufacter',
            new_name='manufacturer',
        ),
    ]
