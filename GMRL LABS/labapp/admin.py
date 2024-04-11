from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Staff,Section,Appointment,Enquiry,Contactus

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    verbose_name_plural = 'Staff'

class CustomUserAdmin(UserAdmin):
    inlines = (StaffInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Section)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'age', 'created', 'updated']
    list_per_page = 10



class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','Appo_date','Appo_time','age','message','created','updated']
    list_per_page=10
admin.site.register(Appointment,AppointmentAdmin) 



class ContactusAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message','created','updated']
    list_per_page=10
admin.site.register(Contactus,ContactusAdmin) 


class EnquiryAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message','created','updated']
    list_per_page=10
admin.site.register(Enquiry,EnquiryAdmin) 


