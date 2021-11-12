# Generated by Django 3.2.6 on 2021-08-24 11:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Enter the name of the assessment', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('classID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('subject', models.CharField(help_text='subject students are studying (e.g. Chemistry)', max_length=254)),
                ('course', models.CharField(help_text='Course the students are studying (e.g. Btec Level 3 in Applied Science)', max_length=254)),
                ('year', models.IntegerField(help_text='year of study (e.g. 1 or 2)')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('date', models.DateTimeField()),
                ('lessonID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('context', models.TextField(help_text='Enter the context of the lesson', max_length=5000)),
                ('objectives', models.TextField(help_text='Enter the objectives of the lesson', max_length=5000)),
                ('learner_needs', models.TextField(help_text='Enter the how the needs of the learners are met in the lesson', max_length=5000)),
                ('wider_learning', models.TextField(help_text='Enter the how wider learning is achieved in the lesson (e.g. literacy)', max_length=5000)),
                ('extended_learning', models.TextField(help_text='Enter any extra learning needed after the lesson (e.g. homework)', max_length=5000)),
                ('classID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lessonplanner.class')),
            ],
        ),
        migrations.CreateModel(
            name='StudentActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Enter the name of the activity', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LessonActivities',
            fields=[
                ('componentID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('start_time', models.IntegerField(help_text='When does the activity start')),
                ('end_time', models.IntegerField(help_text='When does the activity end')),
                ('order', models.IntegerField(help_text='where does the activity come in the lesson')),
                ('activity', models.CharField(help_text='Enter starter, main or plenary', max_length=254)),
                ('teacher_activity', models.TextField(help_text='Enter what the teacher is doing', max_length=5000)),
                ('assessment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lessonplanner.assessment')),
                ('lessonID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lessonplanner.lesson')),
                ('student_activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lessonplanner.studentactivity')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lessonplanner.teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='lessonplanner.teacher'),
        ),
    ]
