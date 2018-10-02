from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import redirect,render
from django import forms
from rest_framework import generics
from django.views import View
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.forms import ModelForm
from django import forms
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.db.models import Q
from datetime import datetime as dt
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework import serializers
from PIL import Image
from studentprojms.models import *
def home(request):
    projects=project.objects.all().filter(status=1)
    return render(request,'home.html',{'projects':projects})

class projectform(forms.Form):
    projname = forms.CharField(max_length=128)
    projdesc = forms.CharField(max_length=1000)
    branch = forms.CharField(max_length=100)
    topic = forms.CharField(max_length=20)
    studname1 = forms.CharField(max_length=128)
    stuid1 = forms.CharField(max_length=12)
    contact1=forms.CharField(max_length=10)
    email1=forms.CharField(max_length=40)
    studname2 = forms.CharField(max_length=128,required=False)
    stuid2 = forms.CharField(max_length=12,required=False)
    contact2 = forms.CharField(max_length=10,required=False)
    email2 = forms.CharField(max_length=40,required=False)
    studname3 = forms.CharField(max_length=128,required=False)
    stuid3 = forms.CharField(max_length=12,required=False)
    contact3 = forms.CharField(max_length=10,required=False)
    email3 = forms.CharField(max_length=40,required=False)

def Addproject(request):
    if request.method == 'POST':
        form = projectform(request.POST)

        # import ipdb
        # ipdb.set_trace()
        if form.is_valid():
            name1,name2,name3=form.cleaned_data['studname1'],form.cleaned_data['studname2'],form.cleaned_data['studname3']
            id1,id2,id3=form.cleaned_data['stuid1'],form.cleaned_data['stuid2'],form.cleaned_data['stuid3']
            c1,c2,c3=form.cleaned_data['contact1'],form.cleaned_data['contact2'],form.cleaned_data['contact3']
            e1,e2,e3=form.cleaned_data['email1'],form.cleaned_data['email2'],form.cleaned_data['email3']
            p=project(projname=form.cleaned_data['projname'],projdesc=form.cleaned_data['projdesc'],studname1=name1,studname2=name2,studname3=name3,stuid1=id1,stuid2=id2,stuid3=id3,branch=form.cleaned_data['branch'],topic=form.cleaned_data['topic'],contact1=c1,contact2=c2,contact3=c3,email1=e1,email2=e2,email3=e3)
            p.save()

            return redirect('/home/')
    else:
        form = projectform()
    return render(request, 'newproj.html', {'form': form})

def viewstudproject(request,id):
    p=project.objects.get(id=id)
    l=[]
    if p.studname1 !='0':
        l.append({'name':p.studname1,'roll':p.stuid1,'cnt':p.contact1,'email':p.email1})
    if p.studname2 !='0':
        l.append({'name':p.studname2,'roll':p.stuid2,'cnt':p.contact2,'email':p.email2})
    if p.studname3 !='0':
        l.append({'name':p.studname3,'roll':p.stuid3,'cnt':p.contact3,'email':p.email3})
    return render(request,'viewstudproj.html',{'p':p,'students':l,'cnt':len(l)})

class studentmarksform(forms.Form):
    m1 = forms.IntegerField()
    m2 = forms.IntegerField()
    m3 = forms.IntegerField()
    m4 = forms.IntegerField()
    m5 = forms.IntegerField()
    m6 =forms.IntegerField()
    m7 = forms.IntegerField()
    m8 = forms.IntegerField()
    m9 = forms.IntegerField()
    m10 = forms.IntegerField()

def Studentmarks(request,id,stuid):
    if request.method=='POST':
        form = studentmarksform(request.POST)
        if form.is_valid():
            m1 = form.cleaned_data['m1']
            m2 = form.cleaned_data['m2']
            m3 = form.cleaned_data['m3']
            m4 = form.cleaned_data['m4']
            m5 = form.cleaned_data['m5']
            m6 = form.cleaned_data['m6']
            m7 = form.cleaned_data['m7']
            m8 = form.cleaned_data['m8']
            m9 = form.cleaned_data['m9']
            m10 = form.cleaned_data['m10']
            if not studmarks.objects.filter(stuid=stuid):
                m = studmarks(stuid=stuid, m1=m1, m2=m2, m3=m3, m4=m4, m5=m5, m6=m6, m7=m7, m8=m8, m9=m9, m10=m10)
                m.save()
            else:
                m=studmarks.objects.get(stuid=stuid)
                m.m1=m1
                m.m2=m2
                m.m3=m3
                m.m4=m4
                m.m5=m5
                m.m6=m6
                m.m7=m7
                m.m8=m8
                m.m9=m9
                m.m10=m10
                m.save()
            return redirect('viewstudproj',id)
    else:
        form = studentmarksform()
        formd = {}
        formd['m1'] = ""
        formd['m2'] = ""
        formd['m3'] = ""
        formd['m4'] = ""
        formd['m5'] = ""
        formd['m6'] = ""
        formd['m7'] = ""
        formd['m8'] = ""
        formd['m9'] = ""
        formd['m10'] = ""
        if studmarks.objects.filter(stuid=stuid):
            print("exists")
            s=studmarks.objects.get(stuid=stuid)
            formd['m1']=s.m1
            formd['m2']=s.m2
            formd['m3'] = s.m3
            formd['m4'] = s.m4
            formd['m5'] = s.m5
            formd['m6'] = s.m6
            formd['m7'] = s.m7
            formd['m8'] = s.m8
            formd['m9'] = s.m9
            formd['m10'] = s.m10
        return render(request, 'studentmarksform.html', {'form': form,'formd':formd,'stuid':stuid})
    return render(request,'studentmarksform.html',{'stuid':stuid})
