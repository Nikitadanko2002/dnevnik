from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    grade = models.IntegerField()

    def __str__(self):
        return self.full_name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)

    grade = models.PositiveSmallIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name}: {self.grade}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)




    date = models.DateField()
    presence = models.BooleanField(default=True)  # True - присутствие, False - прогул

    def __str__(self):
        if self.subject:
            subject_name = self.subject.name
        else:
            subject_name = "Unknown Subject"
        return f"{self.student.full_name} - {subject_name} - {self.date}: {'Присутствовал' if self.presence else 'Прогул'}"


