from django.db import models
from django .contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    stud_id = models.CharField(max_length=10,null=False,blank=False)
    email = models.EmailField()
    mob_no=models.IntegerField(null=True)
    password=models.CharField(max_length=10)
    date_of_birth=models.DateField(null=True)
    users=models.OneToOneField(User,on_delete=models.CASCADE)



class Warden(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    warden_id = models.CharField(max_length=10,null=False,blank=False)
    email = models.EmailField()
    mob_no=models.IntegerField(null=True)
    password=models.CharField(max_length=10)
    date_of_birth=models.DateField(null=True)
    users=models.OneToOneField(User,on_delete=models.CASCADE)

class Gatepasses(models.Model):
    option=(
        ('1','accepted'),
        ('0','rejected'),
    )
   
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    stud_id=models.CharField(max_length=10,null=False,blank=False)
    date_out=models.DateField(null=True)
    time_out=models.TimeField(null=True)
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=10)
    warden_approve=models.CharField(max_length=3,choices=option)
    date_in=models.DateField(null=True)
    time_in=models.TimeField(null=True)
    users=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    



