# Generated by Django 2.2.12 on 2020-04-24 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
