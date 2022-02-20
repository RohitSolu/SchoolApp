from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Student, Subject
from .forms import SearchForm, StudentForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
# from pathlib import Path
# import sys
from weasyprint import HTML


def index(request):
    return render(request, 'student/adminLogin.html')


def teacher_login(request):
    return render(request, 'student/teacher_login.html')

@login_required(login_url = 'login')
def home(request):
    return render(request,'student/home.html')

@login_required(login_url = 'login')
def addStudent(request, pk):
    form = StudentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        #Create
        filled_form = StudentForm(request.POST)
        if filled_form.is_valid():
            student = Student()
            student.name = filled_form.cleaned_data['name']
            student.fathers_name = filled_form.cleaned_data['fathers_name']
            student.mothers_name = filled_form.cleaned_data['mothers_name']
            student.cls = filled_form.cleaned_data['cls']
            student.grade = filled_form.cleaned_data['grade']
            student.date_of_birth = filled_form.cleaned_data['date_of_birth']
            student.date_of_exam = filled_form.cleaned_data['date_of_exam']
            student.date_of_issue = filled_form.cleaned_data['date_of_issue']
            student.character_of_student = filled_form.cleaned_data['character_of_student']
            student.issuer = filled_form.cleaned_data['issuer']
            student.save()
       



    return render(request, 'student/addStudent.html', {'form':form, 'search_form':search_form})
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username,password = form.cleaned_data.get('username'),form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

class CreateRecord(generic.CreateView):
    model = Student
    fields = ['name','fathers_name','mothers_name','address','cls','grade','date_of_birth','date_of_exam','date_of_issue','character_of_student','issuer']
    template_name = 'student/create_detail.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect('home')

class CreateSubject(generic.CreateView):
    model = Subject
    fields = ['name','cls','subject_code','subjects','credit_hour','grade_point','grade','final_grade','remarks','total_gpa']
    template_name = 'subject/create_subject.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect('home')

class DetailRecord(generic.DetailView):
    model = Student
    success_url = 'student/student_detail.html'

class UpdateRecord(generic.UpdateView):
    model = Student
    fields = ['name','fathers_name','mothers_name','address','cls','grade','date_of_birth','date_of_exam','date_of_issue','character_of_student','issuer']
    template_name = 'student/student_update.html'
    success_url = reverse_lazy('home')

class UpdateSubject(generic.UpdateView):
    model = Subject
    fields = ['name','cls','subject_code','subjects','credit_hour','grade_point','grade','final_grade','remarks','total_gpa']
    template_name = 'subject/subject_update.html'
    success_url = reverse_lazy('home')


class DeleteRecord(generic.DeleteView):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('home')

class DeleteSubject(generic.DeleteView):
    model = Subject
    template_name = 'subject/subject_delete.html'
    success_url = reverse_lazy('home')

class SearchResultsView(ListView):
    model = Student
    template_name = 'student/search_results.html'
    # queryset = City.objects.filter(name__icontains='Pokhara') # new
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        student_list = Student.objects.filter(
            Q(name__icontains=query)
        )
        return student_list


class DetailSubject(generic.DetailView):
    model = Subject
    success_url = 'subject/subject_detail.html'


login_required(login_url = 'login')
def detailMarksheet(request):
    students = Student.objects.all()
    id = students.name
    subjects = Subject.objects.filter(name=str(id))
    return render(request,'subject/subject_detail.html', {'students': students, 'subjects': subjects} )

# class DetailMarkSheet(generic.DetailView):
#     model = Subject
#     success_url = 'student/marksheet.html'


@login_required(login_url = 'login')
def allStudent(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student/all_detail.html',context)


@login_required(login_url = 'login')
def detailSubject(request):
    return render(request, 'subject/marksheet_page.html')
@login_required(login_url = 'login')
def detailSubject2(request):
    return render(request, 'subject/marksheet_page2.html')



class SearchSubjectResultsView(ListView):
    model = Subject
    template_name = 'subject/search_subject.html'
    # queryset = City.objects.filter(name__icontains='Pokhara') # new
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        subject_list = Subject.objects.filter(
            Q(name__icontains=query)
        )
        return subject_list  

class SearchPrintSubjectResultsView(ListView):
    model = Subject
    template_name = 'subject/print.html'
    # queryset = City.objects.filter(name__icontains='Pokhara') # new
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        subjects_list = Subject.objects.filter(
            Q(name__icontains=query)
        )
        return subjects_list  

