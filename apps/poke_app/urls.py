"""
DON'T GET LOST.
YOU ARE IN APP LEVEL URLS FOR THE POKE APP

"""
from django.conf.urls import url
from . import views

def test(request):
    print """

        EYE OF THE TIGER!

    """


urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^give/(?P<id>\d+)$', views.give_a_poke),
    url(r'^logout$', views.logout)
    
]