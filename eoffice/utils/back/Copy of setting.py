#coding:utf-8
import sys
from django.contrib.auth.models import User
from apps.setting.models import AppModule
from django.contrib.contenttypes.models import ContentType

class Module():
    name=""
    url = "/"
    
    def __init__(self, name, url):
        self.name=name
        self.url=url
        
class App():
    name=""
    url = "/"
    app = ""
    modules={}
    
    def __init__(self, name, url):
        self.name=name
        self.url=url
        
    def getName(self):
        return self.name
        
    def addModule(self, name, module):
        self.modules[name]=module
        
    def getModules(self):
        """
        print "len = " + str(len(self.modules))
        print "viewkeys = " + str(list(self.modules.viewkeys()))
        print "viewvalues = " + str(list(self.modules.viewvalues()))
        """
        
        return self.modules
        
    def getModule(self, name):
        """
        print "len = " + str(len(self.modules))
        print "viewkeys = " + str(list(self.modules.viewkeys()))
        print "viewvalues = " + str(list(self.modules.viewvalues()))
        """
        return self.modules.get(name)
        
class Project:
    name = "E-Office"
    company_name = "Багануур ХК"
    home_name=""
    home_url=""
    apps={}
    
    def __init__(self, site_name, company_name, home_name, home_url):
        self.site_name=site_name
        self.company_name=company_name
        self.home_name=home_name
        self.home_url=home_url
        
    def addApp(self, name, app):
        
        self.apps[name]=app
        
       
    def getApps(self):
        """
        print "len = " + str(len(self.apps))
        print "viewkeys = " + str(list(self.apps.viewkeys()))
        print "viewvalues = " + str(list(self.apps.viewvalues()))
        """
        return self.apps
        
    def getApp(self, name):
        return self.apps.get(name)
        
class Page:
    title = ""
    title2 = ""
    user = ""
    menu = ""
    
    breadcrumbs=""
    
    template=""
    
    now_app = ""
    now_app_name = ""
    now_app_url = ""
    
    now_module = ""
    now_module_name = ""
    now_module_url = ""
    
    now_action = ""
    now_action_name = ""
    now_action_url = ""
    
    def printAll(self):
        print "title="+self.title
        print "title2="+self.title2
        print "user="+self.user
        print "menu="+self.menu
        print "breadcrumbs="+self.breadcrumbs
        print "template="+self.template
        
class MainPage:
    
    page = Page
    project = Project
    
    def __init__(self, project):
        self.project=project
        
        
    def getPage(self, request, app_name, module_name, action_name):
        
        self.page.title = self.project.name
        self.page.title2 = self.project.company_name
        
        if request.user.is_authenticated():
            self.page.is_login=True
            self.page.user = User.objects.get(id=request.user.id)
        else:
            self.page.is_login=False
            self.page.user=None
        
        
        
        
        return self.page
        
    def createBreadCrumbs(self):
        pass
        #return self.page.breadcrumbs
    
site_name =""
company_name = "Багануур ХК"

# ============== Project =====================
project = Project(site_name, company_name, "Нүүр", "/")

# ============== App =====================
app_home        = App("home", "/")
app_hrms        = App("hrms", "/hrms/")
app_setting     = App("setting", "/setting/")
app_lesson      = App("lesson", "/lesson/")
app_poll        = App("poll", "/polls/")

module_index   = Module("index", "")
module_config   = Module("config", "config/")
module_module   = Module("module", "module/")


project.addApp(str(app_home.name),      app_home)

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
page1 = pages.getPage("home", "index", "index")
page1.printAll
page2 = pages.getPage("setting", "config", "index")
page2.printAll
page3 = pages.getPage("setting", "config", "list")
page3.printAll

"""