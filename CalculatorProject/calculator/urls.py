
from django.urls import path
from calculator import views
urlpatterns = [
    path('', views.Calculate,name="home"),
    path('calculate', views.Calculate,name="calculate"),

]
