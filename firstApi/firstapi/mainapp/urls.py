from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)
# router.register(r'list', ListCombinedViewSet, basename='user')

urlpatterns = [
    # path('total_list/', ListList.as_view() , name='total_list'),
    # path('list_detail/<int:pk>/', ListDetail.as_view() , name='list_detail'),
    path('',include(router.urls)),
    # path('login/', LoginView.as_view(),name='login')
]
