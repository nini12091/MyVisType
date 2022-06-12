from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='user_login'),
    path('logout/', views.signout, name='user_logout'),
]