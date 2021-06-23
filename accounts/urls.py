
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send-login-email'),
]
