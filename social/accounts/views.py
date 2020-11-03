# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import  reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserCreateForm
from django.contrib.auth import login, logout

from django.shortcuts import render

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'