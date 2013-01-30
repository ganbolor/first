#coding:utf-8
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.setting.models import AppModule

from utils import Project, App, Module, MainPage

site_name =""

company_name = "Багануур ХК"

# ============== Project =====================
project = Project(site_name, company_name, "Нүүр", "/")

# ============== App =====================

#print ContentType.objects.values_list('app_label')


apps = AppModule.objects.filter(is_lock=True)
#apps = ContentType.objects.order_by('app_label').values_list('app_label').distinct()

for item1 in apps:
    app = App(item1.short_name, item1.app, "/"+str(item1.app)+"/")
    project.addApp(app)
    models = ContentType.objects.filter(app_label = str(item1.app))
    
    if models:
        for item2 in models:
            m1   = Module(item2.model, item2.name, item2.model+"/")
            app.addModule(m1)
            m1=""
    else:
        
        models=[]
        
#print project.printProject()


"""
#print "reverse = ["
#for q1 in q:
#    print "  "+q1
#print "]"

apps = ContentType.objects.all()

for app in apps:
    print app.pk, app.app_label, app.model



app_hrms        = App("hrms",    "/hrms/")
app_setting     = App("setting",  "/setting/")
app_lesson      = App("lesson",   "/lesson/")
app_poll        = App("poll",     "/polls/")

module_index   = Module("index", "")
module_config   = Module("config", "config/")
module_module   = Module("module", "module/")


#project.addApp(str(app_home.name),     app_home)

project.addApp(str(app_hrms.name),      app_hrms)
project.addApp(str(app_setting.name),   app_setting)
project.addApp(str(app_lesson.name),    app_lesson)
project.addApp(str(app_poll.name),      app_poll)

print project.getApps()

#print "setting = "+str('setting' in project.apps)
#print "setting = "+str(project.apps['setting'])

project.apps['home'].addModule(str(module_index.name), module_index)
project.apps['setting'].addModule(str(module_config.name), module_config)
project.apps['setting'].addModule(str(module_module.name), module_module)

print project.apps['setting'].getModules()

pages = MainPage(project)
"""

pages = MainPage(project)



"""
page1 = pages.getPage("home", "index", "index")
page1.printAll
page2 = pages.getPage("setting", "config", "index")
page2.printAll
page3 = pages.getPage("setting", "config", "list")
page3.printAll

"""