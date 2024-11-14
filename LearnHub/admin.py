from django.contrib import admin
from .models import Course, Module, Lesson, Assignment, Submission, Quiz, Question, Enrollment, InstructorProfile, Discussion, Menu,MenuItem


# Register your models here.
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Enrollment)
admin.site.register(InstructorProfile)
admin.site.register(Discussion)
admin.site.register(Menu)
admin.site.register(MenuItem)