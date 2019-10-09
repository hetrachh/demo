from django.shortcuts import render,redirect
from django.forms import ModelForm
# Create your views here.
from .models import Student

# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['Enrollment','Fname','Lname','Email']


def addStudent(request, templet_name='student_add.html'):
    form = Student(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student:student:manage')
    return render(request, templet_name, {'form': form})




