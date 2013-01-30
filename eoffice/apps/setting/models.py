#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from utils.const import *

def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)



class AppModule(models.Model):
    name=models.CharField(u"Нэр", max_length = 20, unique = True,)
    
    short_name=models.CharField(u"Товч нэр", max_length = 20, unique = True,)
    desc=models.CharField(u"Тайлбар", max_length = 100, unique = True,)
    link=models.CharField(u"Хаяг", max_length = 100, unique = True, help_text=" Англи үсгээр бичих, '/' тэмдэгтээр эхлэх хэрэгтэй. Жишээ: /home ")
    app=models.CharField(u"App", max_length = 100, unique = True, help_text=" Англи үсгээр хэрэгтэй. Жишээ: home ")
    
    image=models.ImageField(u"Зураг", upload_to=upload_to, null = True, blank = True, )
    thumb=models.ImageField(u"Зураг", upload_to=upload_to, null = True, blank = True, )
    
    show_order=models.IntegerField(u"Дараалал", unique = False, null = True, blank = True, )
    is_lock=models.BooleanField(u"Зөвшөөрөх", null = False, default = False, unique = False,)
    
    insert_user = models.ForeignKey(User, verbose_name=u"Оруулсан хэрэглэгч", null = False)
    insert_date = models.DateTimeField(u"Оруулсан огноо", auto_now_add = True, null = False)
    
    update_user = models.ForeignKey(User, verbose_name=u"Зассан хэрэглэгч", null = True, blank = True, related_name= "update_user")
    update_date = models.DateTimeField(u"Зассан огноо", auto_now = True, null = True)
    
    class Meta:
        #db_table = 'config_config'
        ordering = ["show_order", "name"]
        #verbose_name = u""
        #verbose_name_plural = u"Системийн тохиргоо"
        verbose_name = u"Програм"
        verbose_name_plural = u"Програмууд"
    def __unicode__(self):
        return "%s " % (self.name)
    
    
    
    def save(self, *args, **kwargs):
        self.link = "/"+self.app+"/"
        super(AppModule, self).save(*args, **kwargs)
    
class ContectType(models.Model):
    id = models.OneToOneField(ContentType)
    name = models.CharField(u"Нэр", null = False, blank = False, max_length=255)
    is_view = models.BooleanField(u"Харуулах", default=False)
    
    class Meta:
        #db_table = 'config_config'
        ordering = ["name"]
        #verbose_name = u""
        #verbose_name_plural = u""
        
    def __unicode__(self):
        return "%s " % (self.name)
        
        
class Config(models.Model):
    CONFIG_TYPE_CHOICES = (
        (CONFIG_TYPE_INTEGER, u'бүхэл тоон утга'),
        (CONFIG_TYPE_FLOAT, u'бутархай тоон утга'),
        (CONFIG_TYPE_PERCENT, u'хувь'),
        (CONFIG_TYPE_TEXT, u'текст'),
        (CONFIG_TYPE_ACCOUNT, u'данс'),
        (CONFIG_TYPE_PARENT_ACCOUNT, u'эцэг данс'),
        (CONFIG_TYPE_MENU_ACCOUNT, u'дансны төрөл'),
        (CONFIG_TYPE_MATERIAL_TYPE, u'бараа материалын төрөл'),
        (CONFIG_TYPE_USER, u'хэрэглэгчийн төрөл'),
        (CONFIG_TYPE_JOB_POSITION, u'албан тушаалын төрөл'),
        (CONFIG_TYPE_DOCUMENT, u'баримт бичиг'),
    )
    app = models.ForeignKey(AppModule, verbose_name=u"Модул", null = True)
    label_name = models.CharField(u"Нэр", null = False, blank = False, max_length=255)
    code_name = models.CharField(u"Код нэр", unique = True, null = False, blank = False, max_length=255)
    type = models.CharField(u"Утгын төрөл", max_length = 3, choices = CONFIG_TYPE_CHOICES)
    
    #module = models.CharField(u"Модул", max_length = 3, choices = MODULE_TYPE_CHOICES)
    value = models.TextField(u"Утга")
    
    is_editable = models.BooleanField(u"Засах боломжтой эсэх", null = False, default = True)
    
    insert_user = models.ForeignKey(User, verbose_name=u"Бүртгэсэн хэрэглэгч", null = False)
    insert_date = models.DateTimeField(u"Бүртгэсэн огноо", auto_now_add = True, null = False)
    
    update_user = models.ForeignKey(User, verbose_name=u"Сүүлд засвар оруулсан хэрэглэгч", null = True, blank = True, related_name= "update_user2")
    update_date = models.DateTimeField(u"Сүүлд засвар оруулсан огноо", auto_now = True, null = True)
    
    class Meta:
        #db_table = 'config_config'
        ordering = ["app"]
        verbose_name = u"Системийн тохиргоо"
        verbose_name_plural = u"Системийн тохиргоонууд"
    
    def __unicode__(self):
        return "%s " % (self.label_name)
    
