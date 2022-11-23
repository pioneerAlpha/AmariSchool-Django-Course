from django import template
register=template.Library()
import pytz
from django.utils import timezone
import tzlocal

@register.filter
def convert_to_localtime(utctime):
  fmt='%d %B, %Y %I:%M %p'
  ltz = tzlocal.get_localzone()
  localtz = utctime.replace(tzinfo=pytz.utc).astimezone(ltz)
  return localtz.strftime(fmt)
