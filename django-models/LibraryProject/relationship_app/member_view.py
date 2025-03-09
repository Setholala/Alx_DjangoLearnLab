from django.shortcuts import render
from .utils import role_required

def member_dashboard(request):
    return render(request, 'member_dashboard.html')
