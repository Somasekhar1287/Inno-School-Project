# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:29:00 2021

@author: eagle
"""


from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="homepage"
urlpatterns=[
    path("",views.index,name="index")
    ]

urlpatterns+=staticfiles_urlpatterns()