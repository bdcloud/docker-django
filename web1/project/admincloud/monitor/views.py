# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
import os

# Create your views here.

def index(request):
    dispStr = os.environ.get('DISP_STR')
    return HttpResponse(dispStr)

