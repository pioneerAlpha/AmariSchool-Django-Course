from django.urls import path
from gql_api import views


urlpatterns = [
    path('', views.home, name='home'),
]
