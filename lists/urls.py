from django.urls import path

from lists import views

urlpatterns = [
    path('new', views.new_list, name='new-list'),
    path('<int:list_id>/', views.view_list, name='view-list'),
]
