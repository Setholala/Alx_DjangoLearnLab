from django.shortcuts import render
from .utils import role_required

def Member(request):
    return render(request, 'member_dashboard.html')
