# Generated by Django 4.1 on 2023-11-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encoder', '0003_remove_usermessage_encoded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='text',
            field=models.TextField(max_length=120),
        ),
    ]