"""tourGalway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url

from accounts import views as accounts_views
from tourGalwayWebsite import views
from django.contrib.auth import views as auth_views

urlpatterns=[]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^forum/$', views.forum, name='forum'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^food/$', views.food, name='food'),
    url(r'^ptv/$', views.ptv, name='ptv'),
    url(r'^transport/$', views.transport, name='transport'),
    url(r'^forum/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^forum/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^forum/(?P<board_pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_message, name='topic_message'),
    url(r'^forum/(?P<board_pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('i18n/', include('django.conf.urls.i18n')),

)
