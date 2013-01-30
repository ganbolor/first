#coding:utf-8
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()





#@register.inclusion_tag('polls/index1.html', takes_context = True)
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

#@register.inclusion_tag('polls/index1.html', takes_context = True)
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

#register.filter('cut', cut)
#register.filter('lower', lower)


@register.filter
@stringfilter
def upper(value):
    return value.upper()
    
@register.filter(is_safe=True)
def add_xx(value):
    return '%sxx' % value

@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=None):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<strong>%s</strong>%s' % (esc(first), esc(other))
    return mark_safe(result)

