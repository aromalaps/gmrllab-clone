from django.urls import path,include
from .import views

urlpatterns = [
    
     path('',views.Home,name='home'),
     path('aboutus/',views.AboutUs,name='aboutus'),
     path('packages/',views.Package,name='package'),
     path('blog/',views.Blog,name='blog'),
     path('gallery/',views.Gallery,name='gallery'),
     path('branches/',views.Branches,name='branch'),


]

