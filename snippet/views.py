from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, User

# Create your views here.
def home(request):
    return render(request, "snippet/home.html")