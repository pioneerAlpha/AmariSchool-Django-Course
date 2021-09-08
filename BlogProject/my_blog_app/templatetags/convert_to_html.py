from django import template
register=template.Library()
from django_markup.markup import formatter #Package from https://github.com/bartTC/django-markup

@register.filter
def convert_to_html(text):
    return formatter(text, filter_name='markdown')