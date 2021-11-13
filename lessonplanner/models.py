from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # generate urls by reversing url patterns
import uuid


class Teacher(models.Model):
	"""	Model representing the teacher of the lesson and the user of the app """

	teacherID = models.UUIDField(primary_key=True, default=uuid.uuid4) # unique identifier for primary key for each teacher/user

	username = models.CharField(max_length=100, null=True, unique=True)

	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=254, null=True)
	

	def __str__(self):
		""" Formats teacher name last then first """
		return self.username


class Class(models.Model):
	""" Model  giving information on each class """

	classID = models.CharField(primary_key=True, max_length=100) # unique identifier for primary key for each class

	teacher = models.ForeignKey('Teacher', on_delete=models.RESTRICT, null=True)

	subject = models.CharField(max_length=254, help_text='subject students are studying (e.g. Chemistry)')
	course = models.CharField(max_length=254, help_text='Course the students are studying (e.g. Btec Level 3 in Applied Science)')
	year = models.IntegerField(help_text='year of study (e.g. 1 or 2)')

	def __str__(self):
		return self.classID

class Lesson(models.Model):
	""" Model for generating information about a lesson """

	teacher = models.ForeignKey('Teacher', on_delete=models.RESTRICT, null=True)
	classID = models.ForeignKey('Class', on_delete=models.RESTRICT, null=True)
	date = models.DateTimeField(auto_now=False, auto_now_add=False)

	title = models.TextField(max_length=100)

	lessonID = models.AutoField(primary_key=True) # primary key for lessons

	context = models.TextField(max_length=5000, help_text='Enter the context of the lesson')
	objectives = models.TextField(max_length=5000, help_text='Enter the objectives of the lesson')
	learner_needs = models.TextField(max_length=5000, help_text='Enter the how the needs of the learners are met in the lesson')
	wider_learning = models.TextField(max_length=5000, help_text='Enter the how wider learning is achieved in the lesson (e.g. literacy)')
	extended_learning = models.TextField(max_length=5000, help_text='Enter any extra learning needed after the lesson (e.g. homework)')
	

	def __str__(self):
		return self.title


class StudentActivity(models.Model):
	""" Model for generating activity type """

	name = models.TextField(max_length=5000, help_text='Enter the name of the activity')

	def __str__(self):
		return self.name

class Assessment(models.Model):
	""" Model for representing assessment types """
	name = models.TextField(max_length=1000, help_text='Enter the name of the assessment')

	def __str__(self):
		return self.name

class LessonActivities(models.Model):
	""" Model for generating lesson activities """

	componentID = models.UUIDField(primary_key=True, default=uuid.uuid4)
	lessonID = models.ForeignKey('Lesson', on_delete=models.RESTRICT, null=True) # link activity to lesson via ID

	start_time = models.IntegerField(help_text='When does the activity start')
	end_time = models.IntegerField(help_text='When does the activity end')
	order = models.IntegerField(help_text='where does the activity come in the lesson')

	activity = models.CharField(max_length=254, help_text='Enter starter, main or plenary')

	student_activity = models.ForeignKey('StudentActivity', on_delete=models.RESTRICT, null=True) # link activity to student activity via ID
	teacher_activity = models.TextField(max_length=5000, help_text='Enter what the teacher is doing')
	assessment = models.ForeignKey('Assessment', on_delete=models.RESTRICT, null=True) # link activity to assessment via ID

	def __str__(self):
		return self.student_activity

