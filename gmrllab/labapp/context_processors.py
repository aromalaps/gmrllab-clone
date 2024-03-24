from frondpage.models import Our_Tests,TestPackage,Tests,OurTestinomials,Departments,News_and_events,Blogs,Blog_details,Gallery,Branches

def Testpackages(req):
    test_packages=TestPackage.objects.all()
    return dict(test_packages=test_packages)
def Test(req):
    test=Tests.objects.all()
    return dict(test=test) 
def Ourtests(req):
    ourtests=Our_Tests.objects.all()
    return dict(ourtests=ourtests)
def Ourtestinomial(req):
    testinomial=OurTestinomials.objects.all()
    return dict(testinomial=testinomial) 
def Department(req):
    dept=Departments.objects.all()
    return dict(dept=dept)
def NewsandEvent(req):
    news=News_and_events.objects.all()
    return dict(news=news)
def Blog(req):
    blog=Blogs.objects.all()
    return dict(blog=blog)
def Blog_detail(req):
    blog_detail=Blog_details.objects.all()
    return dict(blog_detail=blog_detail)
def Gallerys (req):
    gallery=Gallery.objects.all()
    return dict(gallery=gallery)
def Branch(req):
    branch=Branches.objects.all()
    return dict(branch=branch)

