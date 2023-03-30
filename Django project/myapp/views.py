from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesform,EmailForms
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from Batchproject import settings
import requests
import random
from django.contrib import messages

# Create your views here.

def index(request):
    user=request.session.get('user')
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            username=""
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                username = newuser.cleaned_data.get('username')
                try:
                    unm=userSignup.objects.get(username=username)
                    print("Username already exists!")
                    messages.error(request,messages.error,"Username already exists!")
                except: #userSignup.DoseNotExist
                 newuser.save()
                print("User created successfully!")
                messages.success(request,messages.success,"User created successfully!")
                return redirect('/')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            userid=userSignup.objects.get(username=unm)
            print("UserID:",userid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfull!")
                request.session['userid']=userid.id
                request.session['user']=unm

    ## SMS sending code  ##
                """otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"7567391478"}
                #querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":f"Dear User!\Your account has been logdin\nYour OTP is {otp}","language":"english","route":"q","numbers":request.POST["mobile"]}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)"""
                messages.success(request,f"Welcome! {unm}")
                print(user)
                return redirect('notes')
            else:
                print("Error!Login faild")
                messages.error(requests,"Error! Login faild")
    return render(request,'index.html',{'user':user})

def profile(request):
    uid=request.session.get('userid')
    user=request.session.get('user')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cuser)
            updateuser.save()
            print("Your profile has been updated!")
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':userSignup.objects.get(id=uid)})

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=notesform(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been uploaded!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        feedback=EmailForms(request.POST)
        if feedback.is_valid():
            feedback.save()

            # Email Sending Code
            sub="Thank you!"
            msg=f"Dear user\n\nHiii shruti!\n\nHow are you??"
            fromEmail=settings.EMAIL_HOST_USER
            toEmail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=fromEmail,recipient_list=toEmail)
            print("Your feedback send successfully!")
        else:
            print(feedback.errors)
    return render(request,'contact.html')
"""def contact(request):
    if request.method=='POST':
        feedback=EmailForms(request.POST)
        if feedback.is_valid():
            feedback.save()
            
 #####EMAIL SENDING CODE#####
            sub = "Thank you!!"
            messages =f"Dear user\n\nHiii shruti!\n\nHow are you??"
            fromEmail=settings.EMAIL_HOST_USER
            toEmail=[request.POST['email']]
            send_mail(subject=sub,message=messages,from_email=fromEmail,recipient_list=toEmail)
            print("Your feedback send successfully!!")
        else:
            print(feedback.errors)
            return render(request,'contact.html')
    """
def userlogout(request):
    logout(request)
    return redirect('/')

def adminpage(request):
        user=request.session.get('user')
        return render(request,'adminpage.html',{'user':user})

def alluserdata(request):
    data=userSignup.objects.all()
    return render(request,'alluserdata.html',{'data':data})
