from django.urls import path
from . import views

app_name = 'vis_app'

urlpatterns = [
    path('', views.index, name="index"),
]
