#coding:utf-8
from django.contrib.auth.models import User
#from apps.config.models import AppModule



class Project:
    site_name = ""
    company_name = "Ирмүүн"
    
    apps=[]
    apps2={}
    
    def __init__(self, site_name, company_name):
        self.site_name=site_name
        self.company_name=company_name
    
    def addApp(self, app):
        self.apps.append(app)
        
    def addApp2(self, name, app):
        self.apps2[name]=app
       
    def getAppList(self):
        print self.apps
        return self.apps
    
class Action:
    name=""
    url="/"
    def __init__(self, name, url):
        self.name=name
        self.url=url
        
        
class App(dict):
    name=""
    url = "/"
    
    def __init__(self, name, url):
        self.name=name
        self.url=url
    def getName(self):
        return self.name

class Module:
    app= App
    
    name = ""
    url = ""
    title = ""
    
    action_index=Action("Нүүр", "index/")
    action_list=Action("Жагсаалт", "list/")
    action_view=Action("Харах", "view/")
    action_add=Action("Нэмэх", "add/")
    action_edit=Action("Засах", "edit/")
    action_del=Action("Устгах", "del/")
    
    def __init__(self, app, name, url):
        self.app = app
        self.name = name
        self.url = url
        self.title = self.app.title
    def getUrlIndex(self):
        return self.app.getUrl+self.url+self.action_index.url
    def getUrlList(self):
        return self.app.getUrl+self.url+self.action_list.url
    def getUrlAdd(self):
        return self.app.getUrl+self.url+self.action_add.url
    def getUrlView(self):
        return self.app.getUrl+self.url+self.action_view.url
    def getUrlEdit(self):
        return self.app.getUrl+self.url+self.action_edit.url
    def getUrlDel(self):
        return self.app.getUrl+self.url+self.action_del.url
    def getTitle(self):
        return self.title

class Page:
    
    module = Module
    
    title = ""
    title2=title
    
    url=""
    is_login=False
    user=User
    name = ""
    error=""
    
    def __init__(self, module):
        
        self.module = module
        
        self.title = self.module.title
       
    def setTitle(self, module):
        self.title = str(module.getTitle)
         
    def setPage(self, request, type):
        self.setLogin(request)
        self.setUrl(type)
        
            
    def setLogin(self, request):
        if request.user.is_authenticated():
            self.is_login=True
            self.user = User.objects.get(id=request.user.id)
        else:
            self.is_login=False
            self.user=None
            
    def setUrl(self, type):
        
        if(type=="index"):
            self.url=self.module.getUrlIndex
        elif(type=="add"):
            self.url=self.module.getUrlAdd()
        elif(type=="list"):
            self.url=self.module.getUrlList()
        elif(type=="view"):
            self.url=self.module.getUrlView()
        elif(type=="edit"):
            self.url=self.module.getUrlEdit()
        elif(type=="del"):
            self.url=self.module.getUrlDel()
        
        return self.url
    def getUrl(self):
        return self.url
    
    def isLogin(self, request):
        # return true = login
        # return false = no login
        if request.user.is_authenticated():
            self.is_login=True
            self.user = User.objects.get(id=request.user.id)
        else:
            self.is_login=False
            self.user=None
        return self.is_login




