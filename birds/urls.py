from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [

    path('', LoginView.as_view(template_name='birds/login.html'), name='login'),
    path('birds_list/', views.birds_list, name='birds_list'),
    path('birds_post/', views.bird_post, name='bird_post'),
    path('add_bird_post/', views.add_new_birds, name='add_bird_post'),
    path('bird_detail/<int:pk>/', views.bird_detail, name='bird_detail'),
    path('delete_bird/<int:pk>/', views.delete_bird, name='delete_bird'),
]
