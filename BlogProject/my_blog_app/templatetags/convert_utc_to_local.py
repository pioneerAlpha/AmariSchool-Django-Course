from django import template
register=template.Library()
import pytz
from django.utils import timezone
import tzlocal

@register.filter
def convert_to_localtime(utctime):
  fmt = '%b. %d, %Y %H:%M %p'
  ltz = tzlocal.get_localzone()
  localtz = utctime.replace(tzinfo=pytz.utc).astimezone(ltz)
  return localtz.strftime(fmt)
