from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
path('exams/',views.exams,name='exams'),
path('questions/',views.questions,name='questions'),
]