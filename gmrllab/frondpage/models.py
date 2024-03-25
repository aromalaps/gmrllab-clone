from django.db import models

# Create your models here.
class TestPackage(models.Model):
    package_name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='testpackage')
    tests = models.TextField(help_text='Enter test names separated by commas')
    description=models.TextField()
    def __str__(self):
        return self.package_name

    def get_tests_list(self):
        return [test.strip() for test in self.tests.split(',')]
    
class Tests(models.Model):
    test_type=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.test_type

class Our_Tests(models.Model):
    test_type=models.ForeignKey(Tests, on_delete=models.CASCADE)
    test_name=models.CharField(max_length=150,unique=True)
    testes = models.TextField(help_text='Enter test names separated by commas')
    def __str__(self):
        return self.test_name
    def get_testes_list(self):
        return [Otest.strip() for Otest in self.testes.split(',')]

class News_and_events(models.Model):
    news=models.TextField()
    def __str__(self):
        return self.news


# for carousel departments
class Departments(models.Model):
    dep_name=models.CharField(max_length=150,unique=True)
    dep_image=models.ImageField(upload_to='department/')
    dep_decrption=models.TextField()
    dep_detail_banner=models.ImageField(upload_to='departmentbanner/')
    def __str__(self):
        return self.dep_name
    

class OurTestinomials(models.Model):
    name=models.CharField(max_length=150,unique=True)
    place=models.CharField(max_length=200)
    Description=models.TextField(max_length=300)
    def __str__(self):
        return self.name



    
class Blogs(models.Model):
    blog_number=models.IntegerField(unique=True)
    blog_image=models.ImageField(upload_to='Blogs/')
    subject=models.TextField()

    
class Blog_details(models.Model):
    blog_number=models.ForeignKey(Blogs, on_delete=models.CASCADE)
    blog_heading=models.CharField(max_length=500)
    description=models.TextField()
    def __str__(self):
        return self.blog_heading
    
class Gallery(models.Model):
    image=models.ImageField(upload_to='Gallery/')
    Description=models.TextField()
    

class Branches(models.Model):
    branch_place=models.CharField(max_length=200)
    branch_image=models.ImageField(upload_to='branch/')
    branch_description=models.TextField()
    phone=models.CharField(max_length=13)
    address=models.CharField(max_length=200)
    email=models.EmailField( max_length=254)

    def __str__(self):
        return self.branch_place
    
class Privacy(models.Model):
    heading=models.CharField(max_length=500)
    description=models.TextField()
    def __str__(self):
        return self.heading
class TermsandConditions(models.Model):
    heading=models.CharField(max_length=500)
    description=models.TextField()
    def __str__(self):
        return self.heading
class AboutUs(models.Model):
    heading=models.CharField(max_length=500)
    description=models.TextField()
    def __str__(self):
        return self.heading
