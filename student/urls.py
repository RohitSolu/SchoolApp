from django.urls import path
# from django.contrib import auth
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index,name="index"),
    #search
    path('search/', login_required(views.SearchResultsView.as_view(),login_url = 'login'), name='search_results'),
    #All Students
    path('allStudent',views.allStudent,name="all"),
    path('student/<int:pk>/markSheet',views.detailMarksheet,name="marksheet"),
    path('teacher_login/', views.teacher_login, name="teacher_login"),
    path('home/', views.home, name="home"),

    #Auth
    path('login/signup', views.SignUp.as_view(),name="signup"),
    path('login', auth_views.LoginView.as_view(),name="login"),
    path('signup', auth_views.LogoutView.as_view(),name="logout"),

    #Student
    path('student/createRecord',login_required(views.CreateRecord.as_view(),login_url = 'login'),name="create_record"),
    #Subject
    path('subject/createSubject',login_required(views.CreateSubject.as_view(),login_url = 'login'),name="create_subject"),

    #CRUD
    path('student/<int:pk>',login_required(views.DetailRecord.as_view(),login_url = 'login'),name="detail"),
    #path('subject/<int:pk>',login_required(views.DetailSubject.as_view(),login_url = 'login'),name="detail_subject"),

    path('student/<int:pk>/update',login_required(views.UpdateRecord.as_view(),login_url = 'login'),name="update"),
    path('student/<int:pk>/updateSubject',login_required(views.UpdateSubject.as_view(),login_url = 'login'),name="updateSubject"),

    path('student/<int:pk>/delete',login_required(views.DeleteRecord.as_view(),login_url = 'login'),name="delete"),
    path('subject/<int:pk>/delete',login_required(views.DeleteSubject.as_view(),login_url = 'login'),name="delete_subject"),

    #Add_Student
    path('student/<int:pk>/addstudent',views.addStudent,name="add_student"),

    #Marksheet
    path('home/subject_detail',views.detailSubject, name='detail_for_marks'),
    # path('home/subject_detail', views.search, name='search_subject'),
    path('home/subject_detail/marksheet_detail', login_required(views.SearchSubjectResultsView.as_view(),login_url = 'login'), name='search_subject'),
    # path('search/', login_required(views.SearchResultsView.as_view(),login_url = 'login'), name='search_results'),

    path('home/for_final/print', login_required(views.SearchPrintSubjectResultsView.as_view(),login_url='login'),name='print'),
    #For Final
    path('home/for_final',views.detailSubject2, name='for_final'),
    #path('home/subject_detail/marksheet_detail/print', login_required(views.SearchSubjectResultsView.as_view(),login_url = 'login'), name='print'),






    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)