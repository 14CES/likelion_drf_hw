from django.urls import path
from .views import *
from . import views

app_name = 'singer'

urlpatterns = [
    path('singer', views.singer_list_create),
    path('song', views.song_list_create),
    path('singer/<int:singer_id>', views.singer_detail_update_delete),
    path('song/<int:song_id>', views.song_detail_update_delete),
]