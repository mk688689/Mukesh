# Generated by Django 2.2.5 on 2019-09-07 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20190907_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotepage',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quotepage',
            name='get_started_this_week',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='quotepage',
            name='just_research',
            field=models.BooleanField(default='False'),
        ),
    ]
