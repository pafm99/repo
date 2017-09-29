"""

APP LEVEL URLS
LOG IN APP

"""
from django.conf.urls import url
from . import views

def test(request):
    print """

        WOO HOO PART 2 DONE!

    """


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
    
]