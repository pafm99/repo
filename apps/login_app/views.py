"""

APP LEVEL VIEWS
LOG IN APP

"""

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, datetime
from models import User



# Create your views here.

def index(request):
    return render(request, 'login_app/index.html')
#Registration
def register(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "User was created")
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')
#Log IN
def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, "Email and/or Password are incorrect")
        return redirect('/')
    request.session['email'] = results['user'].email #Stores email in session
    request.session['first_name'] = results['user'].first_name #Stores First Name in Session
    request.session['id'] = results['user'].id #Stores id in sessions.
    return redirect("/poke/dashboard")


def logout(request):
    request.session.flush()
    return redirect('/')