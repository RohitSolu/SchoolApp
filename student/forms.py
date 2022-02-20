from dataclasses import fields
from .models import Student, Subject
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','fathers_name','mothers_name','address','cls','grade','date_of_birth','date_of_exam','date_of_issue','character_of_student','issuer']

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255,label='Search Student:')

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','cls','subject_code','subjects','credit_hour','grade_point','grade','final_grade','remarks','total_gpa']


