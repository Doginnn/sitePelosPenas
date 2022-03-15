from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    count = User.objects.count()
    return render(request, 'index.html', {"count": count})
