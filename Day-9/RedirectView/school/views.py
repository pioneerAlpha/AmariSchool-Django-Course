from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.
class GoogleRedirectView(RedirectView):
    url = "https://www.google.com"
    permanent = True

class HomeRedirectView(RedirectView):
    pattern_name = 'homekey'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        kwargs['pk'] = 70
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)