from django.shortcuts import render, redirect
from labapp.models import Contactus,Appointment,Enquiry  # Assuming your Contactus model is in the same app
# enquiry form is at labapp

def ContactUs(req):
    if req.method == "POST":
        name = req.POST.get('name', '')
        email = req.POST.get('email', '')
        phone = req.POST.get('phone', '')
        subject = req.POST.get('subject', '')
        message = req.POST.get('message', '')
        contact = Contactus(name=name, email=email, phone=phone, subject=subject, message=message)     
        contact.save()
        return redirect('home')
    return render(req, 'contactus.html')  
def MakeAppointment(req):
    if req.method == "POST":
        if 'appoint_form1' in req.POST: 
            name = req.POST.get('name', '')
            email = req.POST.get('email', '')
            phone = req.POST.get('phone', '')
            Appo_date = req.POST.get('date', '')
            Appo_time = req.POST.get('time', '')
            age = req.POST.get('age', '') 
            gender = req.POST.get('gender', '')  
            message = req.POST.get('message', '')
            appointment = Appointment(name=name,email=email,phone=phone,Appo_date=Appo_date,Appo_time=Appo_time,age=age,gender=gender,message=message)     
            appointment.save()
            return redirect('home')
    return render(req, 'appointment.html')


