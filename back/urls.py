from django.urls import path
from .views import categories, home, list_url

urlpatterns = [
    path('', home, name="Home"),
    path('category/<int:id>/', categories, name="Categories"),
    path('playlist/<str:code>/', list_url, name="Playlist"),
    # path('video/<int:id>/', video, name="Video")
]