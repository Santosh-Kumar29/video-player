from django.urls import path
from . import views

urlpatterns = [
    path('save_subtitles/', views.save_subtitles, name='save_subtitles'),
    path('get_subtitles/<str:video_id>/', views.get_subtitles, name='get_subtitles'),
]
