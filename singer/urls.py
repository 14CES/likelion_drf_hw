from django.urls import path
from .views import *
from . import views

app_name = 'singer'

urlpatterns = [
    path('singer', views.singer_list_create),
    path('singer/<int:singer_id>/song', views.song_read_create),
    path('singer/<int:singer_id>', views.singer_detail_update_delete),
]