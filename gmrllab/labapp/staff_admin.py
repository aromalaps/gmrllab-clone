from django.contrib import admin
from .models import Appointment,Enquiry,Contactus

class StaffAdminSite(admin.AdminSite):
    site_header = 'Staff Administration'
    site_title = 'Staff Admin'

staff_admin_site = StaffAdminSite(name='staffadmin')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'Appo_date', 'Appo_time', 'age', 'message', 'created', 'updated']
    list_per_page = 10

staff_admin_site.register(Appointment, AppointmentAdmin)

class ContactusAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message','created','updated']
    list_per_page=10
staff_admin_site.register(Contactus,ContactusAdmin) 


class EnquiryAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message','created','updated']
    list_per_page=10
staff_admin_site.register(Enquiry,EnquiryAdmin) 
