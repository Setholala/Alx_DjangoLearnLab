from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard

urlpatterns = [
    path('list/', list_books, name='list'),
    path('detail/', LibraryDetailView, name='detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),
    path('admin/', views.admin_view, name='admin-view'),
    path('librarian/', views.librarian_view, name='librarian-view'),
    path('member/', views.member_view, name='member-view'),
    path('add-book/', views.add_book_view, name='add-book'),
    path('edit-book/', views.edit_book_view, name='edit-book'),
    path('delete-book/', views.delete_book_view, name='delete-book'),
    ]
