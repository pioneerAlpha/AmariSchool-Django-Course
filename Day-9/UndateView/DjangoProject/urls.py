from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name = 'stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(), name = 'thanks'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name = 'update'),
    path('thanks-update/', views.ThanksUpdateTemplateView.as_view(), name = 'thanks-update'),
]
