# Generated by Django 3.2.6 on 2021-08-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplanner', '0009_alter_teacher_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
