from django.urls import path
from . import views

app_name = 'vis_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('test/<int:test_id>/',views.test, name="test"),
]
