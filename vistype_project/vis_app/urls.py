from django.urls import path
from . import views

app_name = 'vis_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('test/<int:test_id>/',views.test, name="test"),
    path('type/<int:vis_id>/',views.type, name='type'),
    path('finish/',views.finish, name='finish'),
    path('prefer/<int:prefer_id>/',views.prefer, name='prefer'),
    path('user/', views.user_info, name='user_info')
]
