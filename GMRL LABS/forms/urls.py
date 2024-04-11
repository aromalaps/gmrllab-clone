from django.urls import path,include
from .import views

app_name='form'
urlpatterns = [
    path('contactform/',views.ContactUs,name='contactform'),
    path('appoiform/',views.MakeAppointment,name='makeappointment'),
 

]
