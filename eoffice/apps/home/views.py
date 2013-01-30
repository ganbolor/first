#coding:utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from apps.setting.models import Config, AppModule

from utils.setting import pages
app_name="home"

def index(request):
    #шалгах нэвтэрсэн эсэх
    #print request.user
    module="index"
    action="index"
    
    page = pages.getPage(request, app_name, module, action)
    
    
    app_list = AppModule.objects.all()
    
    constant={
        'page': page,
        'app_list': app_list,
        }
    
    return render_to_response('home/index.html', 
                              constant,
                              #context_instance=RequestContext(request)
                              )
    
