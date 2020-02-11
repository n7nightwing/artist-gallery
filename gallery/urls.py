from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('artists/new', views.artist_create, name='artist_create'),
    path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),

    path('creations/', views.creation_list, name='creation_list'),
    path('creations/<int:pk>', views.creation_detail, name='creation_detail'),
    path('creations/new', views.creation_create, name='creation_create'),
    path('creations/<int:pk>/edit', views.creation_edit, name='creation_edit'),
    path('creations/<int:pk>/delete', views.creation_delete, name='creation_delete'),
]