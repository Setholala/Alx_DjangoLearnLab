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
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard')
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    ]
