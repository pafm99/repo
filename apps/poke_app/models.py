# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.
class Poke(models.Model):
    poker = models.ForeignKey(User, related_name='poked')
    pokee = models.ForeignKey(User, related_name='got_poked')