from django.contrib import admin
from .models import Student, Subject, Grade, Attendance


# Регистрация моделей для отображения в админке


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1


class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    inlines = [GradeInline, AttendanceInline]


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Attendance)
