# Generated by Django 2.2.5 on 2019-09-07 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20190907_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotepage',
            name='get_started_this_week',
            field=models.BooleanField(default='False'),
        ),
    ]
