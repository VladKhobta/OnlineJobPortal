# Generated by Django 3.2.9 on 2022-06-06 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_phone_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Type',
            new_name='UserType',
        ),
    ]
