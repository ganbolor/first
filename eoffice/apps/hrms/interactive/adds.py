#coding:utf-8
from apps.hrms.interactive.models import Customers, ChangeHistoryCustomers
from utils.globals import ReportBug
def intCustomersInsert(user):
    ret_mes=""
    ret_val=False
    """
    import pymssql
    conn = pymssql.connect(host='192.168.10.1', user='user1', password='higanaa', database='BaganuurHRMS')
    
    cur = conn.cursor()
    cur.execute("SELECT TOP 10 * FROM View_ssCustomers ORDER BY ActionDate DESC  ")
    row = cur.fetchone()
    ids=0
    
    print "==================================="
    print "            START FOR READ"
    
    while row:
        ids=ids+1
        print "%d, ID=%d, Name=%s" % (ids, row[0], row[1])
        check=None
        try:
            check=IntCustomers.objects.get(CustomerID = str(row[1]))
        except Exception, e:
            print "Error code: a3asdfF"
            print e
        
        print "check = " + str(check)
        
        if(check):
            a=check
            a.InsertType="u"
        else:
            a=IntCustomers()
            a.InsertType="i"
        '''
        print (row[2]).decode('ISO-8859-1').encode('utf8')
        print (row[2]).decode('utf8').encode('ISO-8859-1')
        
        print (row[2]).decode('latin1').encode('utf8')
        print (row[2]).decode('utf8').encode('latin1')
        
        print (row[2]).decode('cp1252').encode('utf8')
        print (row[2]).decode('utf8').encode('cp1252')
        
        print (row[2]).decode('ISO-8859-1')
        print (row[2]).decode('latin-1')
        print (row[2]).decode('latin1')
        print (row[2]).decode('cp1252')
        print (row[2]).decode('cp850')
        
        
        print (row[2]).encode('ISO-8859-1')
        print (row[2]).encode('utf8')
        print (row[2]).encode('latin1')
        print (row[2]).encode('cp1252')
        '''
            
        
        a.CustomerInfID=    str(row[0])
        a.CustomerID=       str(row[1])
        a.DescriptionL=     unicode(row[2]).encode('utf-8')
        a.DescriptionF=     unicode(row[3]).encode('utf-8')
        a.ParentNameL=      unicode(row[4]).encode('utf-8')
        a.ParentNameF=      unicode(row[5]).encode('utf-8')
        a.DepartmentInfID=  str(row[6])
        a.CustomerGroupInfID=str(row[7])
        a.PositionInfID=    str(row[8])
        a.Types=            str(row[9])
        a.ActiveStatus=     str(row[10])
        a.IsExists=         str(row[11])
        a.VATPayer=         str(row[12])
        a.ActionDoneBy=     str(row[13])
        a.ActionDate=       str(row[14])
        a.IsActive=         str(row[15])
        a.SecondCustomerID= str(row[16])
        a.AccountTypeInfID= str(row[17])
        a.LastLoginDate=    str(row[18])
        a.IsContract=       str(row[19])
        a.HireDate=         str(row[20])
        a.add_user=         request.user
        a.edit_user=        request.user
        a.save()
        try:
            a.save()
            print 'update'
            
        except Exception, e:
            print "Error code: 21345sAd"
            print e
            pass
        
        row = cur.fetchone()
    conn.close()
    
    """
    import pyodbc
    
    #if(1):
    try:
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.10.1;DATABASE=baganuurHRMS;UID=user1;PWD=higanaa')
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 10 * FROM View_ssCustomers ")
        rows = cursor.fetchall()
        
        #print rows
        
        for row in rows:
            #print "====================== start"
            
            #for i in row.DescriptionL: print(hex(ord(i)))
            #for i in row.DescriptionF: print(hex(ord(i)))
            #for i in row.ParentNameL: print(hex(ord(i)))
            #for i in row.ParentNameF: print(hex(ord(i)))
            #print "====================== end"
            
            #fo = open("foo.txt", "wb+")
            #print "Name of the file: ", fo.name
            #print "Closed or not : ", fo.closed
            #print "Opening mode : ", fo.mode
            #print "Softspace flag : ", fo.softspace
            #fo.write(unicode(row.DescriptionL).encode('utf-8'))
            
            """
            fo.writelines(unicode(row.DescriptionL).encode('utf-8'))
            fo.writelines(unicode(row.DescriptionF).encode('utf-8'))
            fo.writelines(unicode(row.ParentNameL).encode('utf-8'))
            fo.writelines(unicode(row.ParentNameF).encode('utf-8'))
            """
            
            #fo.writelines("aasdf asdklfj asdf йыбөо рйыбөолр йыбө")
           
            check=None
            try:
                check=Customers.objects.get(CustomerID = str(row.CustomerID))
            except Exception, e:
                pass
            
            ret_value = True
            if(check):
                a=check
                a.InsertType="u"
                
                history=ChangeHistoryCustomers()
                ret_value = history.checkCreateHistory(check, row, user)
                if(ret_value == True):
                    history.save()
                
            else:
                a=Customers()
                a.InsertType="i"
            
            if(ret_value == True):
                a.CustomerInfID=    (row.CustomerInfID)
                a.CustomerID=       (row.CustomerID)
                a.DescriptionL=     unicode(row.DescriptionL).encode('utf-8')
                a.DescriptionF=     unicode(row.DescriptionF).encode('utf-8')
                a.ParentNameL=      unicode(row.ParentNameL).encode('utf-8')
                a.ParentNameF=      unicode(row.ParentNameF).encode('utf-8')
                a.DepartmentInfID=  (row.DepartmentInfID)
                a.CustomerGroupInfID=(row.CustomerGroupInfID)
                a.PositionInfID     =(row.PositionInfID)
                a.Types             =(row.Types)
                a.ActiveStatus=     (row.ActiveStatus)
                a.IsExists=         (row.IsExists)
                a.VATPayer=         (row.VATPayer)
                a.ActionDoneBy=     (row.ActionDoneBy)
                a.ActionDate=       (row.ActionDate)
                a.IsActive=         (row.IsActive)
                a.SecondCustomerID= (row.SecondCustomerID)
                a.AccountTypeInfID= (row.AccountTypeInfID)
                a.LastLoginDate=    (row.LastLoginDate)
                a.IsContract=       (row.IsContract)
                a.HireDate=         (row.HireDate)
                a.add_user=         user
                a.edit_user=        user
                a.save()
            
            #fo.close()
            
            '''
            print str(row.DescriptionL)
            print str(row.DescriptionL.encode("iso-8859-15"))
            
            print str(row.DescriptionL.encode('ISO-8859-1'))
            print str(row.DescriptionL.encode('latin-1'))
            print str(row.DescriptionL.encode('latin1'))
            print str(row.DescriptionL.encode('cp1252'))
            print str(row.DescriptionL.encode('cp850'))
            '''
            
            #a=IntCustomers()
            #a.DescriptionL=     (row.DescriptionL).decode('cp1252')
            #a.save()
        ret_val=True
        ret_mes=u"Success, All user download finished"
    #try:
    #    pass     
    except Exception, e:
        print e
        ret_mes=str(e)
        ReportBug()
        raise
    return ret_val, ret_mes