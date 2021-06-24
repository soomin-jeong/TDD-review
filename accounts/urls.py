
from django.urls import path
from django.contrib.auth import logout
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send-login-email'),
    path('login', views.login, name='login'),
    path('logout', logout, {'next_page': '/'}, name='logout')

]
