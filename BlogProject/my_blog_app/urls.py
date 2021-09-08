from django.urls import path
from my_blog_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home2'),
    path('about_us', views.about_us, name='about_us'),
    path('single_post/<int:pk>', views.single_post, name='single_post'),
    path('contact', views.contact, name='contact'),
    path('write_post', views.write_post, name='write_post'),
    path('update_post/<int:id>', views.update_post, name='update_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('my_blogs', views.my_blogs, name='my_blogs'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('user_profile', views.user_profile, name='user_profile'),
]
