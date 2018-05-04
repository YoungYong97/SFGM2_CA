from django.conf.urls import url 
from django.contrib import admin

#import the views from our boards app
from tourGalwayWebsite import views

#add a pattern is that if no specific request is made, we route to the
#home method in our views.py of our website

urlpatterns = [ 
    url(r'admin/', admin.site.urls),
 ]
