#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

from utils.const import *

def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)

class DemoModule(models.Model):
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
        super(DemoModule, self).save(*args, **kwargs)
    