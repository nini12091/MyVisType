from django.urls import path
from . import views

app_name = 'vis_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('test/<int:test_id>/',views.test, name="test"),
    path('type/<int:vis_id>/',views.type, name='type'),
    path('finish/',views.finish, name='finish'),
    path('prefer/<int:prefer_id>/',views.prefer, name='prefer'),
    path('user/', views.user_info, name='user_info'),
    path('exportcsv_test/', views.exportcsv_test, name="exportcsv_test"),
    path('exportcsv_type/', views.exportcsv_type, name="exportcsv_type"),
    path('exportcsv_prefer/', views.exportcsv_prefer, name="exportcsv_prefer"),
    path('exportcsv_user/', views.exportcsv_user, name="exportcsv_user"),
]
