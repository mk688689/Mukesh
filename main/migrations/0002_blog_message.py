# Generated by Django 2.2.5 on 2019-10-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
