from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('ins/', views.instructor, name='instructor'),
    path('stu/', views.student, name='student'),
    path('dept/', views.department, name='department'),
    path('f1/', views.F1, name='F1'),
    path('f2/', views.F2, name='F2'),
    path('f3/', views.F3, name='F3'),
    path('f4/', views.F4, name='F4'),
    path('f5/', views.F5, name='F5'),
    path('f6/', views.F6, name='F6'),
]
