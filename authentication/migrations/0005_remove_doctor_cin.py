# Generated by Django 3.2.3 on 2021-06-27 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210627_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='cin',
        ),
    ]