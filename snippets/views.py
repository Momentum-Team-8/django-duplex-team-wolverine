from django.shortcuts import render
from .models import Snippet, Tags
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def homepage(request):
    return render(request, "snippets/home.html")