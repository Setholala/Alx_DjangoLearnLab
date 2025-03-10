from django.shortcuts import render
from .utils import role_required

def Librarian(request):
    return render(request, 'librarian_dashboard.html')
