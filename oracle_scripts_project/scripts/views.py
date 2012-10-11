# Create your views here.
from scripts.forms import loginForm
from scripts.forms import basicForm

from django import forms
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response as render
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponseRedirect
import datetime

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

import re
import cx_Oracle

# from django.contrib.auth.models import User
# adding users in django: python manage.py shell
# user = User.objects.create_user('admin', 'admin@admin.com', '123456')
# user.is_staff = True
# user.save()
#User.objects.all().delete()


def home(request):
    if request.user:
        user = request.user
    else:
        user = "AnonymousUser"

    return render("index.html", {
        "user": user,
    }, context_instance=RequestContext(request))

def loginPage(request, cookie):
    if request.POST:
	user1 = User.objects.get(username="admin")
	first_login = False
	if (user1.last_login == user1.date_joined):
	    first_login = True        

        frm = loginForm(request.POST)
        frm_dict = request.POST
        user_email = frm_dict['username']
        username = get_object_or_404(User, email=user_email)
        user = authenticate(username=username, password=frm_dict['passwd'])

        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
		if first_login:
                    return HttpResponseRedirect('/first_configuration/')
		else:                    
                    return HttpResponseRedirect('/admin/')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        frm = loginForm()

        return render("login.html", {
            "frm": frm,
        }, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def admin(request, cookie):
    if request.POST:
        frm = loginForm(request.POST)
        if frm.is_valid():
            frm_dict = request.POST
    else:
        frm = loginForm()

    list_test = [21,43,50,89,45,23]
    list_name = ["db1","db2","db3","db4","db5","db6"]

    return render("admin.html", {
	"lst_val": list_test,
	"lst_nm": list_name,
        "frm": frm,
        "user": request.user,
    }, context_instance=RequestContext(request))


def logoff(request, cookie):
    logout(request)
    return render("logout.html")

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def basic_conf(request):
    if request.POST:
        frm = basicForm(request.POST)
        frm_dict = request.POST
 	user = User.objects.filter(username="admin").update(string_connection=__build_str_conn(frm_dict))	

    else:
	frm = basicForm()

    return render("basic_conf.html", {
	"frm": frm,
    }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def first_conf(request):
    if request.POST:
        frm = basicForm(request.POST)
        frm_dict = request.POST
 	user = User.objects.filter(username="admin").update(string_connection=__build_str_conn(frm_dict))	

    else:
	frm = basicForm()

    return render("first_conf.html", {
	"frm": frm,
    }, context_instance=RequestContext(request))

def __build_str_conn(form_dict):
	return(form_dict['username']+"/"+form_dict['passwd']+'@' + 
     	       "(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)" + 
     	       "(HOST="+form_dict['host']+")(PORT="+form_dict['port']+"))(CONNECT_DATA="+
               "(SERVICE_NAME="+form_dict['sid']+")))")
