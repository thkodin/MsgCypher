# Generated by Django 4.1 on 2023-11-07 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='_decoded',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='_text',
        ),
    ]
