from django.urls import path

from.views import *

urlpatterns = [
    path('',index, name='home'),
    path('publication',publication, name='publication'),
    path('base', base, name='base'),
   
]
