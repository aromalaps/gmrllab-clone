from django.shortcuts import render,get_object_or_404,redirect
from .models import TestPackage,Blog_details,Blogs,Branches,Our_Tests,Tests


# Create your views here.
def Details_Package(req,id):
   test_package = TestPackage.objects.get(id=id)
   tests_list = test_package.get_tests_list()
   detailpackage=TestPackage.objects.get(id=id)
   return render(req, "detailspackage.html",{'detailpackage':detailpackage,'tests_list': tests_list})



def Blog_detail(req,id):
    blog = get_object_or_404(Blogs,id=id)
    blog_details = Blog_details.objects.filter(blog_number=blog)
    return render(req, "blog_details.html", {'blog': blog, 'blog_details': blog_details})


def Branch_detail(req,id):
    branch_detail = Branches.objects.get(id=id)
    return render(req, "branch_details.html",{'branch_detail':branch_detail})

def ATests(req):
    all_our_tests = Our_Tests.objects.all()
    return render(req, 'tests.html', {'all_our_tests': all_our_tests})
# def Details_Test(req):
#     detail_tests = Our_Tests.objects.get()
#     tests_list = detail_tests.get_testes_list()
#     return redirect('tests')




   
