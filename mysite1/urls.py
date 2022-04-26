from django.urls import path
from django.views.generic.base import TemplateView # new

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dept/', views.department, name='department'),
    path('f11/', views.F1_1, name='F1_1'),
    path('f12/', views.F1_2, name='F1_2'),
    path('f13/', views.F1_3, name='F1_3'),
    path('f2/', views.F2, name='F2'),
    path('f3/', views.F3, name='F3'),
    path('f4/', views.F4, name='F4'),
    path('f5/', views.F5, name='F5'),
    path('f6/', views.F6, name='F6'),
	##
    path('main/', views.get_main, name='get_main'),
    path('success/', views.success, name='success'),
    path('admin/', views.get_admin, name='get_admin'),
    path('f1/', views.get_f1, name='get_f1'),
    path('pro/', views.get_professor, name='get_professor'),
    path('stu/', views.get_student, name='get_student'),
    ##
    path('admin_login/', views.login_admin, name='login_admin'),
    path('professor_login/', views.login_professor, name='login_professor'),
    path('student_login/', views.login_student, name='login_student'),
]

