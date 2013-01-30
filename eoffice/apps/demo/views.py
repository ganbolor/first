#coding:utf-8
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from django.contrib.contenttypes.models import ContentType

from apps.setting.models import Config, AppModule
from apps.setting.forms import ConfigAddForm, AppModuleAddForm, ActionForm

#from utils.settings import page_setting_app, page_setting_module, page_setting_config
#from utils.utils import config_page, app_module_page, Module

#page = config_page

#config_module     = Module("Тохиргоо", Config, "/config/config/")
#app_module_module = Module("Модул", AppModule, "/config/app/")

from utils.setting import pages

app_name="setting"

@login_required
def index(request):
    module="index"
    action="index"
    
    page = pages.getPage(request, app_name, module, action)
    
    constant={
        'page': page, 
        
        }
    return render_to_response(app_name+'/index.html', constant, context_instance=RequestContext(request))



@login_required
def appmoduleIndex(request):
    module="appmodule"
    action="index"
    page = pages.getPage(request, app_name, module, action)
    
    #print len(page.breadcrumbs)
    
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'list': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant
                              )



@login_required
def appmoduleList(request):
    module="appmodule"
    action="list"
    
    page = pages.getPage(request, app_name, module, action)
    #page.setListPage("search")
    action_form = ActionForm()
    #request.breadcrumbs('just a view to show some url', request.path)
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'list': app_modules, 
        'action_form': action_form
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              context_instance=RequestContext(request))


@login_required
def appmoduleAdd(request):
    module="appmodule"
    action="add"
    
    page = pages.getPage(request, app_name, module, action)
    
    #list_content_type = ContentType.objects.order_by('app_label').values_list('app_label').distinct()
    
    list_content_type = ContentType.objects.all().order_by('pk')
    #print list_content_type
    
    """
    list_app_module =  AppModule.objects.all()
    
    for item in list_app_module:
        print unicode(item.app)
        #if item.app = ''
        
    for item in list_content_type:
        #print item[0]
        
        #print AppModule.objects.filter(app = item[0])
        
        
        try: 
            AppModule.objects.get(app = item[0])
            print "Done = " + str(item) 
        except Exception, v :
            print "Error = "+ str(v)
        
    """
    
    #page = pages.getPage(request, "setting", "app", "add")
    page.error=""
    if request.method == 'POST': # If the form has been submitted...
        form = AppModuleAddForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            short_name = form.cleaned_data['short_name']
            desc = form.cleaned_data['desc']
            app = form.cleaned_data['app']
            image = form.cleaned_data['image']
            show_order = form.cleaned_data['show_order']
            is_lock = form.cleaned_data['is_lock']
            
            save_item = AppModule(
                            name = name,
                            short_name = short_name,
                            desc = desc,
                            app = app,
                            image = image,
                            show_order = show_order,
                            is_lock= is_lock,
                            insert_user = request.user,
                            )
            try:
                save_item.save()
                page.error=""
                page.info="Амжилтай нэмэв"
            except:
                page.error="Хадгалахад алдаа гарав"
            if page.error:
                pass
            else:
                return HttpResponseRedirect('../') # Redirect after POST
        else:
            page.error="Доорх алдаануудыг засна уу."
    else:
        form = AppModuleAddForm() # An unbound form
    constant={
        'list_content_type': list_content_type,
        'page': page, 
        'form': form,
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              context_instance=RequestContext(request))

    
@login_required
def appmoduleView(request, object_id):
    module="appmodule"
    action="view"
    page = pages.getPage(request, app_name, module, action)
    
    if object_id>0:
        app_module=AppModule.objects.get(id= object_id)
    
    constant={
        'page': page, 
        'item': app_module, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )

@login_required
def appmoduleDel(request, object_id):
    module="appmodule"
    action="del"
    page = pages.getPage(request, app_name, module, action)
    
    
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'app_modules': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )

@login_required
def appmoduleEdit(request, object_id):
    module="appmodule"
    action="edit"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'app_modules': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )

@login_required
def configIndex(request):
    module="config"
    action="index"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    configs=AppModule.objects.all()
    
    constant={
        'page': page, 
        'configs': configs, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )


@login_required
def configList(request):
    module="config"
    action="list"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'app_modules': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )

@login_required
def configView(request):
    module="config"
    action="view"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'app_modules': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )



@login_required
def configAdd(request):
    module="config"
    action="add"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    
    if request.method == 'POST': # If the form has been submitted...
        form = AppModuleAddForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            return HttpResponseRedirect('../') # Redirect after POST
    else:
        form = AppModuleAddForm() # An unbound form
    constant={
        'page': page, 
        'form': form, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )

@login_required
def configDel(request):
    module="config"
    action="del"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'app_modules': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )

@login_required
def configEdit(request):
    module="config"
    action="edit"
    page = pages.getPage(request, app_name, module, action)
    #жагсаалт
    app_modules=AppModule.objects.all()
    
    constant={
        'page': page, 
        'app_modules': app_modules, 
        }
    return render_to_response(app_name+"/"+module+'/'+action+'.html', 
                              constant, 
                              )
