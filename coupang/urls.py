from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('signUp/', views.signUp, name='signUp'),
    path('create/', views.product_create, name='create'),
    path('<str:pk>/', views.product_detail, name='detail'),
    path('<str:pk>/update/', views.product_update, name='update'),
    path('<str:pk>/delete/', views.product_delete, name='delete'),
]