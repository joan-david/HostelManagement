
from django.shortcuts import redirect, render
from .models import Student,Warden,Gatepasses
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def frontpage(request):
    return render(request,'Frontpage.html')

def home(request):
    return render(request,'Home.html')

def about(request):
    return render(request,'About.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email_id = request.POST['email_id']
        mob_no = request.POST['mob_no']
        password= request.POST['password']
        dob= request.POST['dob']
        confirm_password = request.POST['confirm_password']
        
        if confirm_password == password:
             if User.objects.filter(username=username).exists():
                  dic={'user':"username already exists"}
                  return render(request,'Register.html',dic)
             
             elif User.objects.filter(email=email_id).exists():
                  dic={'user':"email already exists"}
                  return render(request,'Register.html',dic)
             
             else:
                new_entry = User.objects.create_user(username=username,email=email_id,password=password)
                new_entry.save()
                



                stud= Student(users=new_entry,fname=fname,lname=lname,email=email_id,mob_no=mob_no,date_of_birth=dob,password=password,stud_id=username)
                stud.save()

                dic={'login':"Registered successfully"}

                return render(request,'Login.html',dic)
             

        
        else:
             
             dic={'user':"Password mismatched"}
             return render(request,'Register.html',dic)
        
    return render(request,'Register.html')

        
def ulogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        try:
            a=Student.objects.get(users=user)
        except:
            a=None

        if a is not None:
            auth.login(request,user)
            
            return redirect(studentpage)
        else:

            dic={'login':"Invalid Login"}
            return render(request,'Login.html',dic)

    return render(request,'Login.html')




def success(request):
    return render(request,'success.html')

def wardenreg(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email_id = request.POST['email_id']
        mob_no = request.POST['mob_no']
        password= request.POST['password']
        dob= request.POST['dob']
        confirm_password = request.POST['confirm_password']
        
        if confirm_password == password:
             if User.objects.filter(username=username).exists():
                  dic={'user':"username already exists"}
                  return render(request,'Wardenreg.html',dic)
             
             elif User.objects.filter(email=email_id).exists():
                  dic={'user':"email already exists"}
                  return render(request,'Wardenreg.html',dic)
             
             else:
                new_entry = User.objects.create_user(username=username,email=email_id,password=password)
                new_entry.save() 

                

                warden= Warden(users=new_entry,fname=fname,lname=lname,email=email_id,mob_no=mob_no,date_of_birth=dob,password=password,warden_id=username)
                warden.save()

                dic={'login':"Registered successfully"}

                return render(request,'Wardenlogin.html',dic)
             
        else:
             
             dic={'user':"Password mismatched"}
             return render(request,'Wardenreg.html',dic)
        
    return render(request,'Wardenreg.html')



def wardenlogin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        try:
            a=Warden.objects.get(users=user)
        except:
            a=None

        if a is not None:
            auth.login(request,user)
            return redirect(wardenpage)
        
        else:
            dic={'login':"Invalid Login"}
            return render(request,'Wardenlogin.html',dic)

    return render(request,'Wardenlogin.html')

    
    

def studentpage(request):
    user=request.user         #user table id
    name=Student.objects.get(users=user)   #student table id      
    Name=name.fname
    Lname=name.lname
    dic={'log':Name,'log1':Lname}
    return render(request,'Studentpage.html',dic)



def wardenpage(request):
    user=request.user         
    name=Warden.objects.get(users=user)        
    Name=name.fname
    Lname=name.lname
    dic={'log':Name,'log1':Lname}
    return render(request,'Wardenpage.html',dic)


def sgatepass(request):
    return render(request,'Sgatepass.html')



def sgprequest(request):
     

     user=request.user
     s=Student.objects.get(users=user)
     ids=s.id
     if request.method == 'POST':
        dateout = request.POST['date']
        timeout = request.POST['time']
        reason = request.POST['reason']
        
        
        gate_entry = Gatepasses(date_out=dateout,
                              time_out=timeout,
                              reason=reason,
                              time_in=None,
                              date_in=None,
                              users_id=ids,
                              fname=s.fname,
                              lname=s.lname,
                              stud_id=s.stud_id,
                              warden_approve=''

                              )
        gate_entry.save()
        return redirect(sgpdisplay)
            

     return render(request,'Sgprequest.html')



def sgpdisplay(request):

    user=request.user
    stud=Student.objects.get(users=user)
    Id=stud.id
    s=Gatepasses.objects.filter(users_id=Id).all()

    dic={'st':s}


    return render(request,'Sgpdisplay.html',dic)



def sgpin(request):

    user=request.user
    stud=Student.objects.get(users=user)
    Id=stud.id
    s=Gatepasses.objects.filter(users_id=Id).filter(warden_approve=1).all()

    dic={'st':s}

    return render(request,'Sgpin.html',dic)

def gatepassin(request,gi):

    a=Gatepasses.objects.filter(id=gi).all()

    dic={'key':a}

    if request.method=="POST":
        datein=request.POST['date']
        timein=request.POST['time']

        Gatepasses.objects.filter(id=gi).update(date_in=datein)
        Gatepasses.objects.filter(id=gi).update(time_in=timein)
        return redirect(sgatepass)

    return render(request,'Student/Gatepassin.html',dic)



def viewsgatepass(request):
    return render(request,'Warden/viewgatepass.html')

def newgatereq(request):
    new=Gatepasses.objects.filter(warden_approve='').all()
    dic={'new':new}
    return render(request,'Warden/Newgatereq.html',dic)


def accepted(request):
    new=Gatepasses.objects.filter(warden_approve='1').all()
    dic={'new':new}
    return render(request,'Warden/Accepted.html',dic)

def rejected(request):
    new=Gatepasses.objects.filter(warden_approve='0').all()
    dic={'new':new}
    return render(request,'Warden/Rejected.html',dic)


def view(request,wk):
    vari=Gatepasses.objects.get(id=wk)
    dic={'var':vari}
    if request.method=='POST':
        v=request.POST['c']
        if v=='1':
            warden=Gatepasses.objects.filter(id=wk).update(warden_approve=1)
            return redirect(viewsgatepass)
        else:
            warden=Gatepasses.objects.filter(id=wk).update(warden_approve=0)
            return redirect(viewsgatepass)

    return render(request,'Warden/View1.html',dic)

def notification(request):
    return render(request,'Notification.html')




