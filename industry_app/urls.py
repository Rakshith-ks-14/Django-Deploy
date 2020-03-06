from django.conf.urls import url
from .views import *

urlpatterns = [

    url('^$',index,name='index'),

    url('^display_laptop$',display_laptop,name='display_laptop'),
    url('^display_mobile$',display_mobile,name='display_mobile'),
    url('^display_desktop$',display_desktop,name='display_desktop'),

    url('^add_desktop$',add_desktop,name='add_desktop'),
    url('^add_mobile$',add_mobile,name='add_mobile'),
    url('^add_laptop$',add_laptop,name='add_laptop'),

    url('^edit_laptop/(?P<pk>\d+)$',edit_laptop,name='edit_laptop'),
    url('^edit_mobile/(?P<pk>\d+)$',edit_mobile,name='edit_mobile'),
    url('^edit_desktop/(?P<pk>\d+)$',edit_desktop,name='edit_desktop'),

    url(r'^delete_laptop/(?P<pk>\d+)$',delete_laptop,name='delete_laptop'),
    url(r'^delete_mobile/(?P<pk>\d+)$',delete_mobile,name='delete_mobile'),
    url(r'^delete_desktop/(?P<pk>\d+)$',delete_desktop,name='delete_desktop'),
]
