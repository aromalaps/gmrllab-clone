from django.contrib import admin
from .models import TestPackage,OurTestinomials,Departments,News_and_events,Tests,Our_Tests,Blogs,Blog_details,Gallery,Branches,Privacy
from .models import TermsandConditions,AboutUs
# Register your mod0els here.


admin.site.register( TestPackage )
admin.site.register( Tests )
admin.site.register( Our_Tests )
admin.site.register( OurTestinomials )
admin.site.register( Blogs )
admin.site.register( Blog_details )
admin.site.register( News_and_events )
admin.site.register( Departments )
admin.site.register( Gallery )
admin.site.register( Branches )
admin.site.register( Privacy )
admin.site.register( TermsandConditions )
admin.site.register( AboutUs )

