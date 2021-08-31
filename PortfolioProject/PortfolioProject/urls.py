
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home,name="home"),
    path('login',views.Login,name="login"),
    path('registration',views.Registration,name="registration"),
    path('logout',views.Logout,name="logout"),
    path('dashboard',views.Dashboard,name="dashboard"),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)