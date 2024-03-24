from django.urls import path
from . import views

app_name='frond'

urlpatterns = [
    path('detailspackage/<int:id>',views.Details_Package,name='detailpackage'),
    path('blog_details/<int:id>',views.Blog_detail,name='blogdetails'),
    path('branch_details/<int:id>',views.Branch_detail,name='branch_detail'),
    path('tests/',views.ATests,name='tests'),
]