# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import word
from .models import users_def

admin.site.register(word)
admin.site.register(users_def)
