from django.shortcuts import render
from .utils import role_required

def librarian_dashboard(request):
    return render(request, 'librarian_dashboard.html')
