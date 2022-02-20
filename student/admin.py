from django.contrib import admin
from .models import Student, Subject

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_exam", "cls",)

admin.site.register(Student)
admin.site.register(Subject)

