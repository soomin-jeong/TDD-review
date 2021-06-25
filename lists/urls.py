from django.urls import path

from lists import views

app_name = 'lists'


urlpatterns = [
    path('new', views.new_list, name='new-list'),
    path('users/<email>/', views.my_lists, name='my-lists'),
    path('<int:list_id>/', views.view_list, name='view-list'),
]
