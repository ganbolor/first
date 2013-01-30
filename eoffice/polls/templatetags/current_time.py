#coding:utf-8
import datetime
from django.core import template
from django.core.template import Context, loader

register = template.Library()


def do_current_time(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(u"%r tag requires a single argument" % token.contents.split()[0])
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(u"%r tag's argument should be in quotes" % tag_name)
    return CurrentTimeNode(format_string[1:-1])
    