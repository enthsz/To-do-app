from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login_page, name='login'),
    path('sair/', views.sair_pagina, name='sair'),
    path('signup', views.custom_signup, name='signup'),

    path('', views.index, name='index'),
    path('update-task/<int:pk>/', views.update_task, name='update-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
]
