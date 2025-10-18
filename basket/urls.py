from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('add/', views.order_create, name='order_create'),
    path('edit/<int:pk>/', views.order_update, name='order_update'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('customer/', views.custom_create, name='customer_create'),
]
