from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter(name='currency')
def currency(dollars, default):
  try:
    dollars = round(float(dollars), 0)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])
  except TypeError:
    return default
