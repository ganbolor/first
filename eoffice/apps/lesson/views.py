#coding:utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import datetime

from apps.lesson.models import Blog, Entry, Author

def index(request):
    
    b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    b.save()
    b.name = 'New name'
    b.save()
    
    
    joe = Author.objects.create(name="Joe")
    joe.save()
    ganaa = Author.objects.create(name="Ganaa")
    ganaa.save()
    
    e = Entry(
            blog = b,
            headline = "headline",
            body_text = "<h1>body_text</h1>",
            pub_date = datetime.datetime.now(),
            mod_date = datetime.datetime.now(),
            authors = joe,
            n_comments = 1,
            n_pingbacks = 2,
            rating = 3,
            )
    e.save()
    
    entry = Entry.objects.get(pk=1)
    
    john = Author.objects.create(name="John")
    paul = Author.objects.create(name="Paul")
    george = Author.objects.create(name="George")
    ringo = Author.objects.create(name="Ringo")
    
    entry.authors.add(ganaa)
    entry.authors.add(john, paul, george, ringo)
    
    entry.save()
    
    
    constant={
        
        }
    
    return render_to_response('lesson/index.html', 
                              constant,
                              #context_instance=RequestContext(request)
                              )
    

