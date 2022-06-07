# Generated by Django 3.2.9 on 2022-06-06 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_type_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertype',
            name='id',
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
