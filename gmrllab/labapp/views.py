from django.shortcuts import render,redirect
from .models import Enquiry
from frondpage.models import TestPackage
# Create your views here.
def Home(req):
    if req.method == "POST":
        name = req.POST.get('name', '')
        email = req.POST.get('email', '')
        phone = req.POST.get('phone', '')
        message = req.POST.get('message', '')
        enquiryform = Enquiry(name=name,email=email,phone=phone,message=message)     
        enquiryform.save()
        return redirect('home')
    return render(req,"index.html")

def AboutUs(req):
    return render(req,"about.html")

def Package(req):
    return render(req,"packages.html")




def Blog(req):
    return render(req,"blog.html")
def Gallery(req):
    return render(req,"gallery.html")
def Branches(req):
    return render(req,"branches.html")
# def Enquiryform(req):
#     return render(req,'index.html')
# def ContactUs(req):
#     return render(req,"contactus.html")
# def Appointment(req):
#     return render(req,"appointment.html")


