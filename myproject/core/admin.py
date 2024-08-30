from django.contrib import admin
from .models import Subject, Teacher, Class, Student, Schedule, Grade

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "subject")
    list_filter = ("subject",)
    search_fields = ("first_name", "last_name")

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "year")
    list_filter = ("year",)
    search_fields = ("name",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "student_class")
    list_filter = ("student_class",)
    search_fields = ("first_name", "last_name")

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("day_of_week", "start_time", "end_time", "subject", "student_class", "teacher")
    list_filter = ("day_of_week", "student_class", "teacher")
    search_fields = ("subject_name", "student_class_name", "teacher_first_name", "teacher_last_name")

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "grade")
    list_filter = ("grade", "subject")
    search_fields = ("student_first_name", "student_last_name", "subject_name")