from django.conf.urls import url,include
from django.contrib import admin

from . import views
app_name='logstat'
url (r'^logstat', include(admin.site.urls)),

urlpatterns = [
    url(r'^home',views.home,name='home'),
    url(r'^updstd:(?P<pk>\d+)$',views.UpdStd.as_view(), name="updstd"),
    url(r'^crtstd$',views.create_std, name="crtstd"),
    url(r'^getimg',views.getimg,name='getimg'),
]
