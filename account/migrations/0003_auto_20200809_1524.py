# Generated by Django 3.0.7 on 2020-08-09 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200804_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='کاربر ویژه تا'),
        ),
    ]