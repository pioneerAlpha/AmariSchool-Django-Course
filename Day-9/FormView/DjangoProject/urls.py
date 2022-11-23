from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactFormView.as_view(), name = 'contact'),
    path('success/', views.successView.as_view(), name = 'success')
]
