# Generated by Django 3.2.6 on 2021-08-26 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplanner', '0003_auto_20210826_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
    ]
