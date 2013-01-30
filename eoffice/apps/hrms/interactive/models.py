#coding:utf-8

from django.db import models
from django.contrib.auth.models import User


INPUT_TYPE_CHOICES = (
    ("i", u'Шинээр'),
    ("u", u'Сайжруулалт'),
)

class Customers(models.Model):
    
    CustomerInfID=      models.CharField(max_length=255, null = True, blank = True)
    CustomerID=         models.CharField(max_length=255, null = True, blank = True)
    DescriptionL=       models.CharField(max_length=255, null = True, blank = True)
    DescriptionF=       models.CharField(max_length=255, null = True, blank = True)
    ParentNameL=        models.CharField(max_length=255, null = True, blank = True)
    ParentNameF=        models.CharField(max_length=255, null = True, blank = True)
    DepartmentInfID=    models.CharField(max_length=255, null = True, blank = True)
    CustomerGroupInfID= models.CharField(max_length=255, null = True, blank = True)
    PositionInfID=      models.CharField(max_length=255, null = True, blank = True)
    Types=              models.CharField(max_length=255, null = True, blank = True)
    ActiveStatus=       models.CharField(max_length=255, null = True, blank = True)
    IsExists=           models.CharField(max_length=255, null = True, blank = True)
    VATPayer=           models.CharField(max_length=255, null = True, blank = True)
    ActionDoneBy=       models.CharField(max_length=255, null = True, blank = True)
    ActionDate=         models.CharField(max_length=255, null = True, blank = True)
    IsActive=           models.CharField(max_length=255, null = True, blank = True)
    SecondCustomerID=   models.CharField(max_length=255, null = True, blank = True)
    AccountTypeInfID=   models.CharField(max_length=255, null = True, blank = True)
    LastLoginDate=      models.CharField(max_length=255, null = True, blank = True)
    IsContract=         models.CharField(max_length=255, null = True, blank = True)
    HireDate=           models.CharField(max_length=255, null = True, blank = True)
    
    # 12 Оруулсан хүн
    add_user   = models.ForeignKey(User, verbose_name=u"Бүртгэсэн хэрэглэгч", null = False)
    # 10 Шивэж оруулсан огноо
    add_date     = models.DateTimeField(u"Бүртгэсэн огноо", auto_now_add = True, null = False)
    # 13 Зассан хүн
    edit_user       = models.ForeignKey(User, verbose_name=u"Сүүлд засвар оруулсан хэрэглэгч", null = True, blank = True, related_name= "edit_user")
    # 11 Зассан огноо
    edit_date     = models.DateTimeField(u"Сүүлд засвар оруулсан огноо", auto_now = True, null = True)

    def __unicode__(self):
        return u'%s %s' % (self.DescriptionF, self.ParentNameL)
    
    def save(self, *args, **kwargs):
        
        super(Customers, self).save(*args, **kwargs) # Call the "real" save() method.
        
HISTORY_MAX_LENGTH = 4096 
class ChangeHistoryCustomers(models.Model):
    change_id    = models.CharField(max_length=255)
    history      = models.CharField(max_length=HISTORY_MAX_LENGTH)
    
    
    add_user    = models.ForeignKey(User, verbose_name=u"Бүртгэсэн хэрэглэгч", null = False)
    add_date    = models.DateTimeField(u"Бүртгэсэн огноо", auto_now_add = True, null = False)
    
    
    def addHistory(self, message):
        if(len(self.history) < HISTORY_MAX_LENGTH):
            len_message = len(message)
            
            if (len_message+len(self.history) <= HISTORY_MAX_LENGTH):
                self.history = self.history + message
            
            
    def checkCreateHistory(self, before, after, user):
        self.add_user = user
        ret_status=False
        
        
        if(str(before.CustomerInfID) != str(after.CustomerInfID)):
            now_history = u"CustomerInfID: "+ str(before.CustomerInfID) + " -> " + str(after.CustomerInfID) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(str(before.CustomerID) != str(after.CustomerID)):
            now_history = u"CustomerID: "+ str(before.CustomerID) + " -> " + str(after.CustomerID) + "; "
            self.addHistory(now_history)
            ret_status=True
            
        # TODO: fix error, 'ascii' codec can't decode byte 0xd0 in position 0: ordinal not in range(128)
        """
        if(unicode(before.DescriptionL).encode('utf-8') != unicode(after.DescriptionL).encode('utf-8')):
            now_history = u"DescriptionL: "+ unicode(before.DescriptionL).encode('utf-8') + u" -> " + unicode(after.DescriptionL).encode('utf-8') + u"; "
            self.addHistory(now_history)
            ret_status=True
        if(unicode(before.DescriptionF).encode('utf-8') != unicode(after.DescriptionF).encode('utf-8')):
            now_history = u"DescriptionF: "+ (before.DescriptionF) + u" -> " + unicode(after.DescriptionL).encode('utf-8') + u"; "
            self.addHistory(now_history)
            ret_status=True
        if(unicode(before.ParentNameL).encode('utf-8') != unicode(after.ParentNameL).encode('utf-8')):
            now_history = u"ParentNameL: "+ (before.ParentNameL) + " -> " + str(after.ParentNameL) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(unicode(before.ParentNameF).encode('utf-8') != unicode(after.ParentNameF).encode('utf-8')):
            now_history = u"ParentNameF: "+ (before.ParentNameF) + " -> " + str(after.ParentNameF) + "; "
            self.addHistory(now_history)
            ret_status=True
        """    
            
        if(str(before.DepartmentInfID) != str(after.DepartmentInfID)):
            now_history = u"DepartmentInfID: "+ str(before.DepartmentInfID) + " -> " + str(after.DepartmentInfID) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(str(before.CustomerGroupInfID) != str(after.CustomerGroupInfID)):
            now_history = u"CustomerGroupInfID: "+ str(before.CustomerGroupInfID) + " -> " + str(after.CustomerGroupInfID) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(str(before.PositionInfID) != str(after.PositionInfID)):
            now_history = u"PositionInfID: "+ str(before.PositionInfID) + " -> " + str(after.PositionInfID) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(str(before.Types) != str(after.Types)):
            now_history = u"Types: "+ str(before.Types) + " -> " + str(after.Types) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(before.ActiveStatus != after.ActiveStatus):
            now_history = u"ActiveStatus: "+ str(before.ActiveStatus) + " -> " + str(after.ActiveStatus) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(before.IsExists != after.IsExists):
            now_history = u"IsExists: "+ str(before.IsExists) + " -> " + str(after.IsExists) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(before.VATPayer != after.VATPayer):
            now_history = u"VATPayer: "+ str(before.VATPayer) + " -> " + str(after.VATPayer) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(before.ActionDoneBy != after.ActionDoneBy):
            now_history = u"ActionDoneBy: "+ str(before.ActionDoneBy) + " -> " + str(after.ActionDoneBy) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(before.ActionDate != after.ActionDate):
            now_history = u"ActionDate: "+ str(before.ActionDate) + " -> " + str(after.ActionDate) + "; "
            self.addHistory(now_history)
            ret_status=True
        if(before.IsActive != after.IsActive):
            now_history = u"IsActive: "+ str(before.IsActive) + " -> " + str(after.IsActive) + "; "
            self.addHistory(now_history)
            ret_status=True
        
        if(str(before.SecondCustomerID) != str(after.SecondCustomerID)):
            now_history = u"SecondCustomerID: "+ str(before.SecondCustomerID) + " -> " + str(after.SecondCustomerID) + "; "
            self.addHistory(now_history)
            ret_status=True
        
        if(str(before.AccountTypeInfID) != str(after.AccountTypeInfID)):
            now_history = u"AccountTypeInfID: "+ str(before.AccountTypeInfID) + " -> " + str(after.AccountTypeInfID) + "; "
            self.addHistory(now_history)
            ret_status=True
        
        if(str(before.LastLoginDate) != str(after.LastLoginDate)):
            now_history = u"LastLoginDate: "+ str(before.LastLoginDate) + " -> " + str(after.LastLoginDate) + "; "
            self.addHistory(now_history)
            ret_status=True
        
        if(str(before.IsContract) != str(after.IsContract)):
            now_history = u"IsContract: "+ str(before.IsContract) + " -> " + str(after.IsContract) + "; "
            self.addHistory(now_history)
            ret_status=True
        
        if(str(before.HireDate) != str(after.HireDate)):
            now_history = u"HireDate: "+ str(before.HireDate) + " -> " + str(after.HireDate) + "; "
            self.addHistory(now_history)
            ret_status=True
        
        if (ret_status==True):
            self.change_id = str(before.CustomerID)
        
        return ret_status
        
        """
        a.CustomerInfID     =str(row.CustomerInfID)
        a.CustomerID        =str(row.CustomerID)
        a.DescriptionL      =unicode(row.DescriptionL).encode('utf-8')
        a.DescriptionF      =unicode(row.DescriptionF).encode('utf-8')
        a.ParentNameL       =unicode(row.ParentNameL).encode('utf-8')
        a.ParentNameF       =unicode(row.ParentNameF).encode('utf-8')
        a.DepartmentInfID   =str(row.DepartmentInfID)
        a.CustomerGroupInfID=str(row.CustomerGroupInfID)
        a.PositionInfID     =str(row.PositionInfID)
        a.Types             =str(row.Types)
        a.ActiveStatus      =str(row.ActiveStatus)
        a.IsExists          =str(row.IsExists)
        a.VATPayer          =str(row.VATPayer)
        a.ActionDoneBy      =str(row.ActionDoneBy)
        a.ActionDate        =str(row.ActionDate)
        a.IsActive          =str(row.IsActive)
        a.SecondCustomerID  =str(row.SecondCustomerID)
        a.AccountTypeInfID  =str(row.AccountTypeInfID)
        a.LastLoginDate     =str(row.LastLoginDate)
        a.IsContract        =str(row.IsContract)
        a.HireDate          =str(row.HireDate)
        """
        
    