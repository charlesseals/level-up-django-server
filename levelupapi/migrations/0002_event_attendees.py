# Generated by Django 4.1.6 on 2023-02-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(through='levelupapi.EventGamer', to='levelupapi.gamer'),
        ),
    ]
