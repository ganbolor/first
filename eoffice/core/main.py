

class Page():
    title=""
    header=""
    user=None
    
    
class AppPage(Page):
    app_name=""
    module=None
    type=None
    
    def getIndexPage(self):
        
        return None
    
class ModulePage(AppPage):
    module_name=""
    ribbon_menu=""
    
    type_index=""
    type_add=""
    type_list=""
    type_edit=""
    type_view=""
    type_delete=""
    
    def getIndexPage(self):
        return None
    
    def getAddPage(self):
        return None
    
    def getListPage(self):
        return None
    
    def getEditPage(self):
        return None
    
    def getViewPage(self):
        return None
    
    def getDeletePage(self):
        return None
    
