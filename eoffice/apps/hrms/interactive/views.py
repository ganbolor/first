#coding:utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from apps.hrms.interactive.models import Customers, ChangeHistoryCustomers
from apps.hrms.interactive.adds import intCustomersInsert

from utils.setting import pages

app_name="hrms"

def index(request):
    module="interactive"
    action="index"
    
    page = pages.getPage(request, app_name, module, action)
    
    constant={
        'page': page,
        
        }
    
    return render_to_response('hrms/interactive/index.html', 
                              constant
                              )
    
    
def list(request):
    module="interactive"
    action="list"
    page = pages.getPage(request, app_name, module, action)
    # TODO: error message
    check=True
    status=True
    message=""
    
    if(check==True):
        status, message=intCustomersInsert(request.user)
    page.status=status
    if(status):
        page.messege=message
    else:
        page.error=message
    
    all_list = Customers.objects.all()[:30]
    
    constant={
        'page': page,
        'list': all_list
        }
    
    return render_to_response('hrms/interactive/intCustomers/list.html', 
                              constant
                              )
    
    
