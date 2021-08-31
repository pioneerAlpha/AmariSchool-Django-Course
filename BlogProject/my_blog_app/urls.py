from django.urls import path
from my_blog_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home2'),
    path('about_us', views.about_us, name='about_us'),
    path('single_post/<int:pk>', views.single_post, name='single_post'),
    path('contact', views.contact, name='contact'),
    path('write_post', views.write_post, name='write_post'),
]
