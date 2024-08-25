from django.urls import path
from . import views

urlpatterns = [
    path('', views.filme_list, name='filme_list'),
    path('filme/<int:pk>/', views.filme_detail, name='filme_detail'),
    path('filme/new/', views.filme_create, name='filme_create'),
    path('filme/<int:pk>/edit/', views.filme_update, name='filme_update'),
    path('filme/<int:pk>/delete/', views.filme_delete, name='filme_delete'),
]
