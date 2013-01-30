
"""
If you want just the line number:

tb = sys.exc_info()[2]
print tb.tb_lineno

You may also have a look at the traceback module, e. g.:

traceback.print_exc()
"""

def ReportBug(request=None, serno=None):
    try:
        import sys
        import traceback
        import os

        # Mail the admins with the error
        exc_info = sys.exc_info()

        if exc_info:
            _file, _line, _func, _line = traceback.extract_tb(exc_info[2])[0]
            _file = os.path.basename(_file)

        else:
            _file, _line, _func, _line = (None, None, None, None)


        # Check if we have a serno
        if not serno:
            from hashlib import md5
            import random
            serno = md5()
            serno.update(str(random.random()))
            serno = serno.hexdigest()

        # When DEBUG is False, send an error message to the admins.
        subject = 'Exception in %s (line %s) (ID: %s)' % (
            _file,
            _line,
            serno
        )

        message = 'Traceback:\n%s\n\n' % ('\n'.join(traceback.format_exception(*exc_info)),)
        print " ====================== ReportBug ======================= "
        print message
        import sys
        from django.views.debug import ExceptionReporter
        from django.http import HttpRequest
        from django.conf import settings
        from django.core.mail import EmailMultiAlternatives
        if not request:
            h = HttpRequest()
            h.META['SERVER_NAME'] = 'FAKE'
            h.META['SERVER_PORT'] = '80'
        else:
            h = request
            
        exp = sys.exc_info()
        t = ExceptionReporter(h, *exp)
        """
        subject, from_email, to = '[Django] %s'%(str(exp[1])), _FROM, _TO
        text_content = message
        html_content = t.get_traceback_html()
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        """
    except Exception, e:
        #mail_admins("SERIOUS ERROR", "Not sure what happened.. %s"%str(e), fail_silently=True)
        
        print e