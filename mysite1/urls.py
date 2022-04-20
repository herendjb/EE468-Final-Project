from django.urls import path

from . import views

urlpatterns = [
    path('josh/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('ins/', views.instructor, name='instructor'),
    path('stu/', views.student, name='student'),
    path('dept/', views.department, name='department'),
]