# Generated by Django 2.1.7 on 2019-02-22 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180527_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='label',
        ),
    ]
