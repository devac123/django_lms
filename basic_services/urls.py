from django.urls import path
from . import views
urlpatterns = [
    path('img_to_base64/', views.image2base64, name="img_to_base64"),
]