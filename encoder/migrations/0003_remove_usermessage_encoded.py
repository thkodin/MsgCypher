# Generated by Django 4.1 on 2023-11-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0002_rename__encoded_usermessage_encoded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='encoded',
        ),
    ]