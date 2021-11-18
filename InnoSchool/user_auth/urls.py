# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:38:53 2021

@author: eagle
"""

from django.urls import path
from . import views

app_name="user_auth"
urlpatterns=[
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("signout",views.signout,name="signout")
    
    ]