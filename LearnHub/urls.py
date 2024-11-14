from django.urls import path,include
from . import views


urlpatterns = [
    path('cources/',views.cource_list, name= 'cources_listing'),
    path('cources/<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),
    path('profile/', views.profile_view, name='profile'),
    path('course/<int:course_id>/lessons/', views.course_lessons, name='course_lessons'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    
]
