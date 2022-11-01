from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name = 'stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(), name = 'thanks'),
    path('detail/<int:pk>', views.StudentDetailView.as_view(), name = 'detail')
]
