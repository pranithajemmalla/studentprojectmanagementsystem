from django import forms
from django.shortcuts import render,redirect,reverse,get_object_or_404
from studentprojms.models import *
from django.http import HttpResponse,JsonResponse

class Adminloginform(forms.Form):
    LoginId = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

def AdminLogin(request):
    if request.method == 'POST':
        form =Adminloginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['LoginId']
            pwd=form.cleaned_data['password']
            if(username=='cvr' and pwd=='hod'):
                return redirect('/adminpage/')
            return render(request, 'adminlogin.html', {'form': form})
    else:
        form = Adminloginform()
    return render(request, 'adminlogin.html', {'form': form})

def adminpage(request):
    reviewers=faculty.objects.all()
    projects=project.objects.all().filter(status=0)
    #projects=projreviewers.objects.values('projid').annotate('projid').count()
    return render(request,'admin.html',{'reviewers':reviewers,'projects':projects})

def Approveproj(request):
    if request.method=="GET":
        pid = request.GET['pid']
        proj=project.objects.get(id=pid)
        proj.status=1
        proj.save()

        return HttpResponse('Success!!')
    else:
        return HttpResponse("Failed!!")
def adminprojects(request):
    projects=project.objects.all().filter(status=0)
    return render(request,'adminpage2.html',{'projects':projects})