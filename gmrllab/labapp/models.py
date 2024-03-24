from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.name
class Staff(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    age = models.IntegerField()
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=13, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)  # Auto set on creation
    updated = models.DateTimeField(auto_now=True)  # Auto set on update

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone = models.CharField(max_length=13)
    Appo_date = models.DateField()
    Appo_time = models.TimeField()
    age = models.IntegerField()
    gender=models.CharField(max_length=150)
    message=models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)  # Auto set on creation
    updated = models.DateTimeField(auto_now=True)  # Auto set on update

    
    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=13)
    message=models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)  # Auto set on creation
    updated = models.DateTimeField(auto_now=True)  # Auto set on update

    
    def __str__(self):
        return self.name


class Contactus(models.Model):
    name = models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=13)
    subject=models.CharField(max_length=150)
    message=models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)  # Auto set on creation
    updated = models.DateTimeField(auto_now=True)  # Auto set on update

    def __str__(self):
        return self.name


