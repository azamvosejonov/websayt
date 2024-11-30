from django.urls import path

from .views import home_paje_view, fanlar_paje_view, studend_paje_view, add_subject_view, add_student_view,add_grade_view

urlpatterns=[
    path('',home_paje_view,name='bosh_sahifa'),
    path('fanlar/',fanlar_paje_view,name='barcha_sahifa'),
    path('studend/',studend_paje_view,name='barcha_oquvchilar'),
    path('fanq/',add_subject_view,name='sub_add'),
    path('oquvchiq/', add_student_view, name='stu_add'),
    path('oquvchib/', add_grade_view, name='gra_add')

]