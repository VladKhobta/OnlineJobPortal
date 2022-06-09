# Generated by Django 3.2.9 on 2022-06-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_usertype_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
