from django.shortcuts import render
from .forms import Reg_form,Login,Feed_form
from .models import Course,Batch,Registration,Feedback
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request,"home.html")

def get_reg(request):
    if request.method=='GET':
        ob=Reg_form()
        return render(request,"reg.html",{'form':ob})
    if request.method=='POST':
        obj=Reg_form(request.POST)
        if obj.is_valid():
            Name=obj.cleaned_data['uname']
            Course=obj.cleaned_data['course']
            Batch=obj.cleaned_data['batch']
            PW=obj.cleaned_data['pwd']
            # CPW=obj.cleaned_data['cpwd']
            # print(Name)
            # print(Course)
            # print(Batch)
            # print(PW)
            # print(CPW)
            e=Registration(uname=Name,course=Course,batch=Batch,pwd=PW)
            e.save()
            print("saved")
    return render(request,"reg.html",{'form':obj})

def get_login(request):
    if request.method=='GET':
        ob=Login()
        return render(request,"login.html",{'form':ob})
    if request.method=='POST':
        obj=Login(request.POST)
        if obj.is_valid():
            Name=obj.cleaned_data['uname']
            PW = obj.cleaned_data['pwd']
            # print(Name)
            # print(PW)
            query=Registration.objects.filter(uname=Name).filter(pwd=PW)
            if(query):
                print("success")

                request.session['user']=Name
                return get_feed(request)
                # return render(request,"logout.html",{})
            else:
                print("pw not valid")
            # e=Registration(uname=Name,pwd=PW)
            # e.save()
            # print("saved")
    # return render(request,"login.html",{'form':obj})
def log_out(request):
    if request.method=='GET':
        ob=Login()
        return render(request,"login.html",{'form':ob})
def get_feed(request):
    if request.method=='GET':
        ob=Feed_form()
        print(request.session['user'])
        return render(request,"feed.html",{'form':ob})
    if request.method=='POST':
        obj=Feed_form(request.POST)
        if obj.is_valid():
            Topic=obj.cleaned_data["topic"]
            Feed=obj.cleaned_data['feedback']
            # print(Topic)
            # print(Feedback)
            # e=Feedback(topic=Topic,feedback=Feed)
            # e.save()
            # print("saved successfully")
            # e=Feedback(feedback=Feed)
            # e.save()
            e=obj.save(commit=False)
            e.save()
            print("saved feedback")
            return render(request,"feed2.html",{})
    return render(request,"feed.html",{})
def feed_back2(request):
    if request.method=='GET':
        return render(request,"feed2.html")