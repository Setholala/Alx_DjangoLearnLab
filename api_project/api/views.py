# BookViewSet handles all CRUD operations for the Book model.
# It is protected using IsAuthenticated permission,
# which means only logged-in users with a valid token can access these endpoints.

from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
     permission_classes = []

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
