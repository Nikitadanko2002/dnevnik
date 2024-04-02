from django.shortcuts import render
from .models import Student, Subject, Grade, Attendance

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

from django.shortcuts import render, redirect
from .models import Student, Subject, Grade, Attendance

def add_grade(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        grade = request.POST.get('grade')
        comment = request.POST.get('comment')
        student = Student.objects.get(pk=student_id)
        subject = Subject.objects.get(pk=subject_id)
        Grade.objects.create(student=student, subject=subject, grade=grade, comment=comment)
        return redirect('students_list')
    return render(request, 'add_grade.html', {'students': students, 'subjects': subjects})

def add_attendance(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST.get('student')
        date = request.POST.get('date')
        presence = request.POST.get('presence')
        student = Student.objects.get(pk=student_id)
        Attendance.objects.create(student=student, date=date, presence=presence)
        return redirect('students_list')
    return render(request, 'add_attendance.html', {'students': students})
