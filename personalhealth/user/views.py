
# Create your views here.
from django.shortcuts import render,redirect
from .models import Registeration,userprofile,myrecord,prescription,hadmin,emergency
from django.http.response import HttpResponse
# Create your views here.
def uhome(request):
    return render(request,'register.html')
def home(request):
    return render(request,'Amain.html')
def register(request): # need to create the function
    if request.method=="POST":
        name=request.POST['name']

        passwor=request.POST['password']
        cpasswor=request.POST['cpassword']
        email=request.POST['email']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        dob=request.POST['dob']
        phone=request.POST['phone']
        healthissue=request.POST['healthissue']
        interest=request.POST['interest']
        context=Registeration.objects.all().filter(email=email).exists()
        if(context==False):
            if(cpasswor==passwor):
                s=Registeration(name=name,password=passwor,email=email)
                s.save()
                r=userprofile(firstname=firstname,lastname=lastname,dob=dob,phone=phone,healthissue=healthissue,interest=interest,email=email)
                r.save()
                return render(request,'login.html')
            else:
                return HttpResponse("please enter the same password and confirmpassword")
        else:
            return HttpResponse("hari great")
   
def login(request):
    if request.method == "POST":
        request.session['email']=request.POST['email']
        password=request.POST['password']
        if Registeration.objects.filter(email=request.session['email'], password=password).exists():
            log=Registeration.objects.get(email=request.session['email'], password=password)
            return render(request,'userhome.html')
        else:
           return render(request,"Error.html")
    else:
        return render(request,'login.html')
def signin(request): # default page
    return render(request,'login.html')
def profile(request): # default page
    return render(request,'profile.html')
def addprofile(request): # need to create the function
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        dob=request.POST['dob']
        phone=request.POST['phone']
        healthissue=request.POST['healthissue']
        interest=request.POST['interest']
        hobby=request.POST['hobby']
        economic_pref=request.POST['economic_pref']
        email=request.session['email']
        s=userprofile(firstname=firstname,lastname=lastname,dob=dob,phone=phone,healthissue=healthissue,interest=interest,hobby=hobby,economic_pref=economic_pref,email=email)
        s.save()
def viewprofile(request):
        email=request.session['email']
        profile={'userprofile':userprofile.objects.all().filter(email=email)}
        return render(request,'profile_list.html',profile)   

def recordupdate(request,id):
    recor={'rec':myrecord.objects.filter(pk=id)}
    return render(request,'updaterecord.html',recor)                   
def updateprofile(request):
    profile={'userprofile':userprofile.objects.all().filter(email=request.session['email'])}
    return render(request,'updateprofile.html',profile)
def updated(request):
    name=request.POST['name']
    lastname=request.POST['lname']
    dob=request.POST['dob']
    phone=request.POST['phone']
    healthissue=request.POST['healthissue']
    interest=request.POST['interest']
    hobby=request.POST['hobby']
    economic_pref=request.POST['economic_pref']
    userprofile.objects.all().filter(email=request.session['email']).update(firstname=name,lastname=lastname,dob=dob,phone=phone,healthissue=healthissue,interest=interest,hobby=hobby,economic_pref=economic_pref)
    return HttpResponse("updated")
def addrecord(request):
    if request.method=="POST":
        email=request.session['email']
        hospitalname=request.POST['hname']
        doctorname=request.POST['dname']
        hospitallocation=request.POST['hlocation']
        diseasename=request.POST['diname']
        date=request.POST['date']
        documentname=request.POST['dtname']
        description=request.POST['desc']
        prescription=request.POST['presc']
        file=request.POST['fil']
        s=myrecord(hospitalname=hospitalname,doctorname=doctorname,hospitallocation=hospitallocation,diseasename=diseasename,date=date,
        documentname=documentname,description=description,prescription=prescription,file=file,email=email)
        s.save()
        return HttpResponse("Record uploaded Successfull")
def rec(request):
    return render(request,'myrecord.html')
def viewrecord(request):
        email=request.session['email']
        Record={'myrecord':myrecord.objects.all().filter(email=email)}
        return render(request,'viewrecord.html',Record)
def emergencydelete(request):
    return redirect('viewemergency.html')
def addprescription(request):
    if request.method=="POST":
        email=request.session['email']
        diseasename=request.POST['diseasename']
        time=request.POST['time']
        mealname=request.POST['meal']
        description=request.POST['description']
        prescript=request.POST['prescriptionname']
        medicinename=request.POST['medicinename']
        s=prescription(diseasename=diseasename,time=time,meal=mealname,description=description,
        prescrip_name=prescript,email=email,medicinename=medicinename)
        s.save()
        return HttpResponse("Record uploaded Successfull")
def pres(request):
    return render(request,'prescription.html')

def viewpres(request):
        email=request.session['email']
        Record={'prescription':prescription.objects.all().filter(email=email)}
        return render(request,'viewprescription.html',Record)

def addemer(request): # default page
    return render(request,'emergency.html')
def addemergency(request): # need to create the function
    if request.method=="POST":
        hospitalname=request.POST['hname']
        location=request.POST['location']    
        phone=request.POST['phone']
        s=emergency(hospitalname=hospitalname,location=location,phone=phone)
        s.save()
        return HttpResponse("Emergency details uploaded Successfully")
def viewemergency(request):
        emergencyview={'emergency':emergency.objects.all()}
        return render(request,'viewemergency.html',emergencyview)
def uviewemergency(request):
        emergencyview={'emergency':emergency.objects.all()}
        return render(request,'uviewemergency.html',emergencyview)
def adminlogin(request):
    if request.method == "POST":
        request.session['email']=request.POST['email']
        password=request.POST['password']
        if hadmin.objects.filter(email=request.session['email'], password=password).exists():
            log=hadmin.objects.get(email=request.session['email'], password=password)
            return render(request,'adminhome.html')
        else:
           return render(request,"Error.html")
    else:
        return render(request,'headlogin.html')
def emerdelete(request,id):
    emer=emergency.objects.get(pk=id)
    emer.delete()
    return redirect("/viewemergency")

def emerupdate(request,id):
    emergen={'emer':emergency.objects.filter(pk=id)}
    return render(request,'updateemergency.html',emergen)

def updateemergency(request): # need to create the function
    if request.method=="POST":
        id=request.POST['id']
        hospitalname=request.POST['hname']
        location=request.POST['location']    
        phone=request.POST['phone']
        emergen={'emer':emergency.objects.get(pk=id)}
        s=emergency.objects.filter(id=id).update(hospitalname=hospitalname,location=location,phone=phone)
        return HttpResponse("Yes")

def recordupdate(request,id):
    recor={'rec':myrecord.objects.filter(pk=id)}
    return render(request,'updaterecord.html',recor)
def presupdate(request,id): # need to create the function
    presc={'pres':prescription.objects.filter(pk=id)}
    return render(request,'updatepres.html',presc)

  

def recordelete(request,id):
    recor=myrecord.objects.get(pk=id)
    recor.delete()
    return redirect("/viewrecord")

def presdelete(request,id):
    pres=prescription.objects.get(pk=id)
    pres.delete()
    return redirect("/viewpres")


def updateprescription(request):
    if request.method=="POST":
        id=request.POST['id']
        email=request.session['email']
        diseasename=request.POST['diseasename']
        time=request.POST['time']
        mealname=request.POST['meal']
        description=request.POST['description']
        prescript=request.POST['prescriptionname']
        medicinename=request.POST['medicinename']
        recor={'rec':prescription.objects.get(pk=id)}
        s=prescription.objects.filter(id=id).update(diseasename=diseasename,time=time,meal=mealname,description=description,
        prescrip_name=prescript,email=email,medicinename=medicinename)
        return HttpResponse("Yes")
def updaterecord(request): # need to create the function
    if request.method=="POST":
        id=request.POST['id']
        hospitalname=request.POST['hname']
        doctorname=request.POST['dname']
        hospitallocation=request.POST['hlocation']
        diseasename=request.POST['diname']
        date=request.POST['date']
        documentname=request.POST['dtname']
        description=request.POST['desc']
        prescription=request.POST['presc']
        file=request.POST['fil']
        email=request.session['email']
        presc={'pres':myrecord.objects.get(pk=id)}
        s=myrecord.objects.filter(id=id).update(hospitalname=hospitalname,doctorname=doctorname,hospitallocation=hospitallocation,diseasename=diseasename,date=date,
        documentname=documentname,description=description,prescription=prescription,file=file,email=email)
        return HttpResponse("Yes")