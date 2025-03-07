from django.urls import path
from .views import list_book, LibraryDetail

urlpatterns = [
    path('list/', list_book, name='list'),
    path('detail/', LibraryDetail, name='detail'),
    ]
