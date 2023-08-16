from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='birds/login.html'), name='login'),  # url для аутентификации
    path('birds_list/', views.birds_list, name='birds_list'),  # url для вывода всех птиц
    path('birds_post/', views.bird_post, name='bird_post'),  # url для добавления записи для конкретной птицы
    path('add_bird_post/', views.add_new_birds, name='add_bird_post'),  # url для добавления птицы
    path('bird_detail/<int:pk>/', views.bird_detail, name='bird_detail'),  # url для вывода информации о птице
    path('delete_bird/<int:pk>/', views.delete_bird, name='delete_bird'),  # url для удаления птицы
]
