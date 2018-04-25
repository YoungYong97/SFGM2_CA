from django.conf.urls import url 
from tourGalwayWebsite import views 
urlpatterns = [ 
url(r'^$', views.HomePageView.as_view()),
 ]
