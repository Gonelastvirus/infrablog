from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.aix_post_detail, name='aix_post_detail'),
    path('redhat/<int:pk>/', views.redhat_post_detail, name='redhat_post_detail'),
     path('redhat/<int:pk>/', views.vmware_post_detail, name='vmware_post_detail'),
   
]

