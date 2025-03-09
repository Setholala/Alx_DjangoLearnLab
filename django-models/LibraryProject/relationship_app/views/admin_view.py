from django.shortcuts import render
from .utils import role_required

@role_required('Admin')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
