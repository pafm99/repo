"""

DON'T GET LOST AGAIN. YOU ARE IN
POKE APP LEVEL VIEWS

"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Count
from models import Poke
from ..login_app.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def dashboard(request):
    print " I wish that I had jessies girl"
    context = {
        'other_users': User.objects.exclude(id=request.session['id']),
        'curr_user': User.objects.get(id=request.session['id']),
        'me': [],
        't': []
    }
    curr_user = User.objects.exclude(id=request.session['id'])
    who_poked = curr_user.all().values('first_name').distinct()
    qwe = curr_user.all().count()
    print qwe
    for user in who_poked:
        context['me'].append(user)
    x = User.objects.values('first_name').annotate(the_count=Count('poked'))
    for y in x:
        context['t'].append(y)
    return render(request, 'poke_app/dashboard.html', context)

def give_a_poke(request, id): #Listening to two things request and the id pass by the link
    print "I like that old time rock and roll!"
    Poke.objects.create(poker = User.objects.get(id=request.session['id']),
    pokee = User.objects.get(id=id))
    return redirect('/poke/dashboard')



def logout(request):
    request.session.flush()
    return redirect('/')



def handler404(request):
    response = render_to_response('404.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response