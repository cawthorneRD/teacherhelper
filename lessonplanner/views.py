from django.shortcuts import render, redirect
from .models import Teacher, Class, Lesson, StudentActivity, Assessment, LessonActivities
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AssessmentForm, StudentActivityForm, ClassForm, LessonForm, LessonActivitiesForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

@login_required
def index(request):
	""" View function for homepage """
	current_user = request.user
		
	users = Teacher.objects.filter(username=current_user)
	
	if not users.exists():
		teacher = Teacher(first_name=current_user.first_name, last_name=current_user.last_name, username=str(current_user.username), email=current_user.email)
		teacher.save()
	
	teacher = Teacher.objects.get(username=current_user)
	
	groups = Class.objects.filter(teacher_id=teacher.teacherID) # gets class details
	
	lesson = Lesson.objects.filter(teacher_id=teacher.teacherID) # gets lesson details
	
	first_name = current_user.first_name
	last_name = current_user.last_name
	
	context = {
		'first_name': first_name,
		'last_name': last_name,
		'groups': groups,
		'lesson': lesson,
				}
	
	return render(request, 'index.html', context=context)

def register(request):
	""" Allows user to register """
	if request.method == 'GET':
		return render(request, 'register.html', {'form': CustomUserCreationForm})

	else:
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
		else:
			return redirect('register')

def get_assessment(request):

	""" Starts the assessment form process """
	if request.method == 'POST':
		form = AssessmentForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = AssessmentForm()
	
	return render(request, 'assessment.html', {'form': form})

def get_student_activity(request):
	""" Starts the student activity form process """
	if request.method == 'POST':
		form = StudentActivityForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = StudentActivityForm()
	
	return render(request, 'student_activity.html', {'form': form})

def get_class(request):
	""" Starts the class form process """
	if request.method =='POST':
		form = ClassForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = ClassForm()

	return render(request, 'class.html', {'form': form})

def get_lesson(request):
	""" Starts the lesson form process """
	if request.method =='POST':
		form = LessonForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = LessonForm()

	return render(request, 'lesson.html', {'form': form})


def get_lesson_activities(request):
	""" Starts the lesson activities form process """
	if request.method =='POST':
		form = LessonActivitiesForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = LessonActivitiesForm()

	return render(request, 'lesson_activities.html', {'form': form})



class lesson_detail(generic.DetailView):
	""" Sets up a page for each lesson gathering all the information from lesson, lesson activities, assessment and student activity """
	model = Lesson

	def get_context_data(self, **kwargs):
        
		context = super(lesson_detail, self).get_context_data(**kwargs)
		context['activity_list'] = LessonActivities.objects.filter(lessonID_id=self.get_object())
		context['assessment_detail'] = Assessment.objects.all()
		context['student_detail'] = StudentActivity.objects.all()

		return context




							