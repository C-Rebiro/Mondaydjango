from django.shortcuts import render
from myapp.form import StudentForm


def home(request):
    stud=StudentForm
    return render(request, 'index.html', {'form': stud})
