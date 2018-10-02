from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

class project(models.Model):
    projname=models.CharField(max_length=128)
    projdesc=models.CharField(max_length=1000)
    branch=models.CharField(max_length=100)
    topic=models.CharField(max_length=20)
    status=models.IntegerField(default=0)
    studname1 = models.CharField(max_length=128)
    stuid1 = models.CharField(max_length=12)
    contact1 = models.CharField(max_length=10)
    email1 = models.CharField(max_length=40)
    studname2 = models.CharField(max_length=128)
    stuid2 = models.CharField(max_length=12,null=True,blank=True)
    contact2 = models.CharField(max_length=10,null=True,blank=True)
    email2 = models.CharField(max_length=40,null=True,blank=True)
    studname3 = models.CharField(max_length=128,null=True,blank=True)
    stuid3 = models.CharField(max_length=12,null=True,blank=True)
    contact3 = models.CharField(max_length=10,null=True,blank=True)
    email3 = models.CharField(max_length=40,null=True,blank=True)
    count=models.IntegerField(default=0,null=True,blank=True)
    date_created = models.DateTimeField(default=timezone.now().replace(microsecond=0))
    report=models.CharField(max_length=128)

class faculty(models.Model):
    fname=models.CharField(max_length=128)
    n=models.IntegerField(default=0)
    subject=models.CharField(max_length=128)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    userid = models.IntegerField(default=0)

class admin(models.Model):
    projectId=models.IntegerField(default=0)
    numreviews=models.IntegerField(default=0)

class projreviewers(models.Model):
    projid=models.IntegerField(default=0)
    reviewerId=models.IntegerField(default=0)

class studmarks(models.Model):
    stuid=models.CharField(max_length=20)
    m1=models.IntegerField(default=0)
    m2 = models.IntegerField(default=0)
    m3 = models.IntegerField(default=0)
    m4 = models.IntegerField(default=0)
    m5 = models.IntegerField(default=0)
    m6 = models.IntegerField(default=0)
    m7 = models.IntegerField(default=0)
    m8 = models.IntegerField(default=0)
    m9 = models.IntegerField(default=0)
    m10 = models.IntegerField(default=0)