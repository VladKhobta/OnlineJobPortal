# Generated by Django 3.2.9 on 2022-06-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='education',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
