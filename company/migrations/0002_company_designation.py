# Generated by Django 3.2.9 on 2022-06-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='designation',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]