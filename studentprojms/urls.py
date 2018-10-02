from django.urls import path
from django.contrib.auth import views
from studentprojms.Views import student,Admin,mentor
urlpatterns=[
    path(r'mentorlogin/', mentor.mentorlogin, name="mentorlogin"),
    path(r'mentorlogout/', views.logout, {'template_name': 'fb/login.html'}, name="logout"),
    path(r'home/',student.home,name="home"),
    path('mentorpage/<int:uid>',mentor.mentorpage,name="mentor"),
    path('addproject/',student.Addproject,name="newproject"),
    path('adminlogin/',Admin.AdminLogin,name="adminlogin"),
    path('adminpage/',Admin.adminpage,name="adminpage"),
    path('addmentor/',mentor.Addmentor,name="addmentor"),
    path('reviewproj/<int:uid>',mentor.Reviewproj,name="reviewproj"),
    path('approveproj/',Admin.Approveproj,name="approveproj"),
    path('adminpage2/',Admin.adminprojects,name="adminprojects"),
    path('viewstudproj/<int:id>',student.viewstudproject,name="viewstudproj"),
    path('studmarksform/<int:id>/<str:stuid>',student.Studentmarks,name="studmarks"),
    path('sendreport',mentor.sendreport,name="sendreport")
]