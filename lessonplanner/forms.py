from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher, Class, Lesson, StudentActivity, Assessment, LessonActivities

class CustomUserCreationForm(UserCreationForm): # creates for for a new user
	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name",)

class AssessmentForm(ModelForm): # form based on Assessment model
	class Meta:
		model = Assessment
		fields = "__all__"

class StudentActivityForm(ModelForm): # form based on StudentActivity model
	class Meta:
		model = StudentActivity
		fields = "__all__"

class ClassForm(ModelForm): # form based on Class model
	class Meta:
		model = Class
		fields = "__all__"

class LessonForm(ModelForm): # form based on Lesson model
	class Meta:
		model = Lesson
		fields = "__all__"

class LessonActivitiesForm(ModelForm): # form based on LessonActivities model
	class Meta:
		model = LessonActivities
		fields = ['lessonID', 'start_time', 'end_time', 'order', 'activity', 'student_activity', 'teacher_activity', 'assessment']