#coding:utf-8
from django.contrib.auth.models import User

test_mode=False

class Module():
    module=""
    name=""
    url = ""
    
    def __init__(self, module,  name,  url):
        self.module=module
        self.name=name
        self.url=url
    
    def getUrl(self):
        return self.url
    
    # ===== index =====
    def getIndexActiontUrl(self):
        return ""
    def getIndexActiontName(self):
        return u"Нүүр"
    
    # ===== add =====
    def getAddActiontUrl(self):
        return "add/"
    def getAddActiontName(self):
        return u"Нэмэх"
    
    # ===== list =====
    def getListActiontUrl(self):
        return "list/"
    def getListActiontName(self):
        return u"Жагсаалт"
    
    # ===== list =====
    def getEditActiontUrl(self):
        return "edit/"
    def getEditActiontName(self):
        return u"Засах"
    
    # ===== view =====
    def getViewActiontUrl(self):
        return "view/"
    def getViewActiontName(self):
        return u"Харах"
    
    # ===== delete =====
    def getDelActiontUrl(self):
        return "del/"
    def getDelActiontName(self):
        return u"Устгах"
    
    def getActionUrl(self, name):
        if name=='index':
            return self.getIndexActiontUrl()
        elif name=='add':
            return self.getAddActiontUrl()
        elif name=='list':
            return self.getListActiontUrl()
        elif name=='edit':
            return self.getEditActiontUrl()
        elif name=='del':
            return self.getDelActiontUrl()
        elif name=='view':
            return self.getViewActiontUrl()
        
    def getActionName(self, name):
        if name=='index':
            return self.getIndexActiontName()
        elif name=='add':
            return self.getAddActiontName()
        elif name=='list':
            return self.getListActiontName()
        elif name=='edit':
            return self.getEditActiontName()
        elif name=='del':
            return self.getDelActiontName()
        elif name=='view':
            return self.getViewActiontName()
    
class App():
    name=""
    app=""
    url = ""
    
    modules=[]
    
    def __init__(self, name, app, url):
        self.modules = []
        self.name=name
        self.app=app
        self.url=url
        
    def getApp(self):
        return self.app
        
    def getName(self):
        return self.name
        
    def addModule(self, module):
        #print "GFGGGGGGGGGGGGGGGGGGGGGGGGG"
        #print '[%s]' % ', '.join(map(str, self.modules))
        self.modules.append(module)
        #print '[%s]' % ', '.join(map(str, self.modules))
    def getModules(self):
        return self.modules
    def printApp(self):
        print "printApp = ["
        print "  app = " + self.app
        print "  url = " + self.url
        #print "  name = " 
        #print self.app.encode('ascii', 'ignore')
        #print unicode(self.name.strip(codecs.BOM_UTF8), 'utf-8')
        #print(u"{0} logs found in %s".format(len(files))) % logdir
        print "  url = " + self.url

        print "  modules = [" 
        for module in self.modules:
            print "    "+module.module
            print "    "+module.url
        print "  ]"
        print "]"
        
    def printModules(self):
        print "printModules = ["
        for key, value in self.modules.items():
            print key, value
        print "]"
        
    def getModule(self, name):
        module = ""
        for item in self.modules:
            if item.module == name:
                module = item
        return module
    
class Project:
    name = "E-Office"
    company_name = "Багануур ХК"
    home_name=""
    home_url=""
    apps=[]
    
    def __init__(self, site_name, company_name, home_name, home_url):
        self.site_name=site_name
        self.company_name=company_name
        self.home_name=home_name
        self.home_url=home_url
        
    def addApp(self, app):
        self.apps.append(app)
        
    def printProject(self):
        print "printProject = ["
        print "  name="+self.name
        print "  company_name="+self.company_name
        #print "  home_name="+self.home_name
        print "  home_url="+self.home_url
        print "  apps="+str(self.apps)
        for item in self.apps:
            print "item = " + str(item)
            item.printApp()
        print "]"

        print "]"
    def getApp(self, name):
        app = ""
        for item in self.apps:
            if item.app == app:
                app = item
        return app
    
    def getApps(self):
        return self.apps
    
    def getAppModules(self, app):
        ret_value=[]
        if app:
            for item in self.apps:
                if item.app == app:
                    ret_value = item.modules
        return ret_value
    
class BreadCrumb(list):

    def __init__(self, url, name):
        self.url = url
        self.name = name
    
class Page:
    title = ""
    title2 = ""
    user = ""
    menu = ""
    
    breadcrumbs=[]
    breadcrumb_urls=[]
    template=""

    now_app = ""
    now_app_url = ""
    now_app_name = ""
    
    now_module = ""
    now_module_url = ""
    now_module_name = ""
    
    now_action = ""
    now_action_url = ""
    now_action_name = ""
    
    project=Project
    
    test_mode=test_mode
    
    
    
       
    def __init__(self):
        self.breadcrumbs=[]
        self.breadcrumb_urls=[]
        #self.myBreadCrumbUrls()
        
    def printAll(self):
        print "title="+self.title
        print "title2="+self.title2
        print "user="+self.user
        print "menu="+self.menu
        print "breadcrumbs="+self.breadcrumbs
        print "template="+self.template
    
    def getApps(self):
        #print "getApps"
        
        return self.project.getApps()
    """
    def myApp(self):
        for app in self.project.getApps():
            if app.name== self.now_app:
                return app
    """  
    def printBreadcrumbs(self):
        for item in self.breadcrumbs:
            print "url="+item.url
            print "name="+str(unicode(item.name).encode('utf-8'))
            
    def listPrint(self, list):
        print "list print ["
        for item in list:
            print "      name  "+str(unicode(item.name).encode('utf-8'))
            print "      url  "+str(item.url)
        print "      ]"
    
    def myBreadCrumbUrls(self):
        #breadcrumbs = self.myBreadCrumbs()
        url = []
        urls=""
        for item in (self.breadcrumbs):
            urls+=item.url
            url.append("<a href='"+urls+"'>"+item.name+"</a>")
        #print str(unicode(url).encode('utf-8'))
        
        self.breadcrumb_urls = url
        
        return url
        
    def myBreadCrumbs(self):
        #print " ========================================== \n myBreadCrumbs"
        #self.printNows()
        #self.printBreadcrumbs()
        breadcrumbs = []
        
        #print self.project.getApps()
        for app in self.project.getApps():
            #print app.name.encode('ascii', 'ignore')
            #print app.app
            #print self.now_app
            if app.app == self.now_app:
                #print "                                  append(app)"
                self.now_app_url = app.url
                self.now_app_name = app.name
                breadcrumbs.append(BreadCrumb(app.url, app.name))
                #print "2"
                #self.listPrint(breadcrumbs)
                
                if self.now_module != "index":
                    for module in app.getModules():
                        
                        if module.module == self.now_module:
                            #print "module  = "+module.module
                            #print "                                  append(module)"
                            
                            self.now_module_url = app.url+module.url
                            self.now_module_name = module.name
                            breadcrumbs.append(BreadCrumb(app.url+module.url, module.name))
                            #print "3"
                            #self.listPrint(breadcrumbs)
                            
                            if self.now_action == "add":
                                action_url= module.getAddActiontUrl()
                                action_name= module.getAddActiontName()
                                
                                self.now_action_url = app.url+module.url+action_url
                                breadcrumbs.append(BreadCrumb(app.url+module.url+action_url, action_name))
                                #print "4"
                                #self.listPrint(breadcrumbs)
                            elif self.now_action == "list":
                                action_url= module.getListActiontUrl()
                                action_name= module.getListActiontName()
                                
                                self.now_action_url = app.url+module.url+action_url
                                breadcrumbs.append(BreadCrumb(app.url+module.url+action_url, action_name))
                                #print "4"
                                #self.listPrint(breadcrumbs)
                            elif self.now_action == "edit":
                                action_url= module.getEditActiontUrl()
                                action_name= module.getEditActiontName()
                                
                                self.now_action_url = app.url+module.url+action_url
                                breadcrumbs.append(BreadCrumb(app.url+module.url+action_url, action_name))
                                #print "4"
                                #self.listPrint(breadcrumbs)
                            elif self.now_action == "del":
                                action_url= module.getDelActiontUrl()
                                action_name= module.getDelActiontName()
                                
                                self.now_action_url = app.url+module.url+action_url
                                breadcrumbs.append(BreadCrumb(app.url+module.url+action_url, action_name))
                                #print "4"
                                #self.listPrint(breadcrumbs)
                            elif self.now_action == "view":
                                action_url= module.getViewActiontUrl()
                                action_name= module.getViewActiontName()
                                
                                self.now_action_url = app.url+module.url+action_url
                                breadcrumbs.append(BreadCrumb(app.url+module.url+action_url, action_name))
                                #print "4"
                                #self.listPrint(breadcrumbs)
                            self.printBreadcrumbs()
                                
        
        self.breadcrumbs=breadcrumbs
        
        #print "count = "+str(len(breadcrumbs))
        self.printBreadcrumbs()
        return self.breadcrumbs
    def getNowApp(self):
        return self.now_app
    
        
    def getNowAppName(self):
        #print "getNowAppName"
        
        
        ret_value=""
        for app in self.project.getApps():
            if app.app == self.now_app:
                ret_value= app.name
                
        return ret_value
    def getNowAppModules(self):
        return self.project.getAppModules(self.now_app)
    
    def getNowModule(self):
        return self.now_module
    
    def getNowAction(self):
        return self.now_action
    
    def getNowAppClass(self):
        print "getNowAppClass"
        
        return self.project.getApp(self.now_app)
    
    def getNowModuleClass(self):
        print "getNowModuleClass"
        now_app_class = self.getNowAppClass()
        
        return now_app_class.getModule(self.now_module)
    
    """
    def getNowModuleListUrl(self):
        print "getNowModuleListUrl"
        now_module_class=self.getNowModuleClass()
        print now_module_class
        return str(self.now_module_url + now_module_class.getListActiontUrl())
    
    def getNowModuleListUrl(self):
        now_module_class = self.getNowModuleClass()
        now_module_class.getActionUrl("list")
    
    
    
    
    def getNowAppUrl(self):
        url = "/"+self.now_app+"/"
        return url
    
    def getNowModuleUrl(self):
        url = self.now_module+"/"
        return url
    
    def getNowActionUrl(self):
        url = self.now_action+"/"
        return url
    
    def setAllUrl(self):
        self.now_app_url=self.getNowAppUrl()
        self.now_module_url=self.getNowModuleUrl()
        self.now_action_url=self.getNowActionUrl()
    """
    def printNows(self):
        print self.now_app + " - " + self.now_app_url
        print self.now_module + " - " + self.now_module_url
        print self.now_action + " - " + self.now_action_url   
        
class MainPage:
    
    
    
    project = Project
    
    def __init__(self, project):
        self.project=Project
        self.project=project
        self.page=Page()
        
    def getPage(self, request, app, module, action):
        
        self.page.title = self.project.name
        self.page.title2 = self.project.company_name
        
        self.page.now_app = app
        self.page.now_module = module
        self.page.now_action = action
        
        #self.page.setAllUrl()
        
        try:
            if request.user.is_authenticated():
                self.page.is_login=True
                self.page.user = User.objects.get(id=request.user.id)
            else:
                self.page.is_login=False
                self.page.user=None
        except Exception, k:
            print "Error, "
            print str(Exception)
            print k
        self.page.project = self.project
        
        self.page.myBreadCrumbs()
        #self.page.myBreadCrumbUrls()
        return self.page
        
    