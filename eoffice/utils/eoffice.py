#coding:utf-8

from utils import Project, App, Module, Action, Page



#=========================================================================
#                  START ALL SETTING
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Project   |    App     |    Module     |    Action     
#+++++++++++++|++++++++++++|+++++++++++++++|++++++++++++++++++++++++++++++
#  eoffice    |            |               |                              
#             | hrms       |               |                              
#             |            | employee      |                              
#             |            | department    |                              
#             |            | position      |                              
#             |            |               |                              
#             |            |               |                              
#             | setting    |               |                              
#             |            |  module       |                              
#             |            |  config       |                              
#             |            |               |                              
#             | lesson     |               |                              
#             |            |               |                              
#             |            |               |                              
#             |            |               |                              

#=========================================================================
site_name ="Е-Оффис"
company_name = "Багануур ХК"

# ============== Project =====================
project = Project(site_name, company_name)

# ============== App =====================

app_home = App(project, "/")
app_hrms = App(project, "/hrms/")
app_setting = App(project, "/setting/")
app_lesson = App(project, "/lesson/")

# ============== Module =====================

# HOME
module_home_home=Module(app_home)

# SETTING
module_setting_module=Module(app_setting, "тодул", "module/")
module_setting_config=Module(app_setting, "тохиргоо", "config/")

# =============== Page ============================
page_home_home=Page("Нүүр", module_home_home)
config_page=Page("Тохиргоо", 2)
hrms_page=Page("Хүний нөөц", 3)
app_module_page=Page("Тохиргоо", 2)


