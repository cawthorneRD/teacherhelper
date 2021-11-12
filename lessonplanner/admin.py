from django.contrib import admin
from .models import Teacher, Class, Lesson, StudentActivity, Assessment, LessonActivities

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(StudentActivity)
admin.site.register(Assessment)
admin.site.register(LessonActivities)
