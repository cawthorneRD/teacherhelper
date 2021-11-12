from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('register/', views.register, name='register'),
	path('assessment/', views.get_assessment, name='assessment'),
	path('student_activity/', views.get_student_activity, name='student_activity'),
	path('class/', views.get_class, name='class'),
	path('lesson/', views.get_lesson, name='lesson'),
	path('lesson_activities/', views.get_lesson_activities, name='lesson_activities'),
	path('detail/<pk>/', views.lesson_detail.as_view(), name='lesson_detail'),
	]
