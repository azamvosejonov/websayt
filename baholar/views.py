

from django.shortcuts import render,redirect
from .models import Grade,Student,Subject
from .forms import AddSubjectFrom,AddStudentFrom,AddGradeFrom



#homepage view
def home_paje_view(request):
    grades=Grade.objects.all()
    context={
        "grades":grades
    }
    return render(request,"home.html",context)


def fanlar_paje_view(request):
    grades=Grade.objects.all()
    context={
        "grades":grades
    }
    return render(request,"fan.html",context)


def studend_paje_view(request):
    grades=Grade.objects.all()
    context={
        "grades":grades
    }
    return render(request,"studend.html",context)


def add_subject_view(request):
    if request.method=='POST':
        form=AddSubjectFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bosh_sahifa')
    else:
        form=AddSubjectFrom()
    context={
        'form':form
    }

    return render(request,"add_subject.html",context)


def add_student_view(request):
    if request.method=='POST':
        form=AddStudentFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bosh_sahifa')
    else:
        form=AddStudentFrom()
    context={
        'form':form
    }

    return render(request,"add_student.html",context)


def add_grade_view(request):
    if request.method=='POST':
        form=AddGradeFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bosh_sahifa')
    else:
        form=AddGradeFrom()
    context={
        'form':form
    }

    return render(request,"add_grade.html",context)





