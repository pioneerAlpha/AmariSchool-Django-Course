from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='dashboard'),
    path('product/', views.product,name='product'),
    path('customer/', views.customer,name='customer'),
    path('customer_details/<str:pk>',views.customerDetails, name='customerDetails'),
    path('products/', views.product, name='product'),
    path('orders/',views.order, name='order'),
    path('userpage/',views.userpage, name='userpage'),
    path('create_order/<str:pk>',views.createOrder,name='createOrder'),
    path('update_order/<str:pk>',views.updateOrder,name='updateOrder'),
    path('delete_order/<str:pk>',views.deleteOrder, name='deleteOrder'),
    path('register/', views.register,name='register'),
    path('login/', views.loginuser,name='login'),
    path('logout', views.logoutuser,name='logout')
]
