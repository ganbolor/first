#coding:utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from decimal import Decimal


from utils.setting import pages
app_name="hrms"

def index(request):
    module="index"
    action="index"
    
    page = pages.getPage(request, app_name, module, action)
    
    constant={
        'page': page,
        
        }
    
    return render_to_response('app/index.html', 
                              constant
                              )
    