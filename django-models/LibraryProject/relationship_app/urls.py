from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list/', list_books, name='list'),
    path('detail/', LibraryDetailView, name='detail'),
    ]
