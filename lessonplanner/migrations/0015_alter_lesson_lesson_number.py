# Generated by Django 3.2.6 on 2021-11-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplanner', '0014_alter_lesson_lesson_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_number',
            field=models.IntegerField(help_text='lesson number', unique=True),
        ),
    ]
