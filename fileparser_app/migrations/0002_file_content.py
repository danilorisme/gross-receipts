# Generated by Django 2.1.3 on 2018-11-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileparser_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='content',
            field=models.TextField(default='No Data'),
        ),
    ]
