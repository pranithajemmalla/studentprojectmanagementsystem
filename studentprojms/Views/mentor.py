from django import forms
from django.shortcuts import render,redirect,reverse,get_object_or_404
from studentprojms.models import *
from django.http import HttpResponse,JsonResponse

class Addmentorform(forms.Form):
    username=forms.CharField(max_length=10)
    password1=forms.CharField(max_length=10)
    password2 = forms.CharField(max_length=10)
    fname = forms.CharField(max_length=128)
    subject = forms.CharField(max_length=128)
    contact=forms.CharField(max_length=10)
    email=forms.CharField(max_length=40)

def Addmentor(request):
    if request.method == 'POST':
        form = Addmentorform(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            u=User(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            u.save()
            # import ipdb
            # ipdb.set_trace()
            user=User.objects.get(username=form.cleaned_data['username'])
            m=faculty(fname=form.cleaned_data['fname'],subject=form.cleaned_data['subject'],userid=user.id,contact=form.cleaned_data['contact'],email=form.cleaned_data['email'])
            m.save()
            #projects=projreviewers.objects.all().filter(reviewerId=request.user.id)
            return redirect('/adminpage/')
    else:
        form = Addmentorform()
    return render(request, 'addmentor.html', {'form': form})

class mentorform(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

def mentorlogin(request):
    if request.method == 'POST':
        form = mentorform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            mentor=User.objects.filter(username=username,password=password).exists()
            # import ipdb
            # ipdb.set_trace()
            if mentor:
                mentor = User.objects.filter(username=username,password=password).first()
                mentor_id=faculty.objects.get(userid=mentor.id)
                return redirect('/mentorpage/'+str(mentor_id.id))
    else:
        form = mentorform()
    return render(request, 'mentorlogin.html', {'form': form})

def mentorpage(request,uid):
    mentor=faculty.objects.get(id=uid)
    #reviewed=projreviewers.objects.all().filter(reviewerId=uid)
    projects = project.objects.all().filter(status=0)
    return render(request,'mentor.html',{'projects':projects,'uid':uid,'mentor':mentor})


def mentorlogout(request):
    if request.method=="post":
        return redirect('/mentorlogin/')

def Reviewproj(request,uid):
    if request.method=="GET":
        pid = request.GET['pid']
        proj=project.objects.get(id=pid)
        proj.count=proj.count+1
        proj.save()
        pr=projreviewers(projid=pid,reviewerId=uid)
        pr.save()
        return HttpResponse('Success!!')
    else:
        return HttpResponse("Failed!!")
def sendreport(request):
    report=request.GET['report']
    pid=request.GET['pid']
    p=project.objects.get(id=pid)
    p.report=report
    p.save()
    return  HttpResponse("suceess")
