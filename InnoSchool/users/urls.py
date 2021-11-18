# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:36:55 2021

@author: eagle
"""

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="users"
urlpatterns=[
    path("",views.index,name="index")
    ]

urlpatterns+=staticfiles_urlpatterns()