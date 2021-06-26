from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, Tags
from django.utils import timezone

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_snippets")
    else:
        return render(request, "snippets/home.html")

@login_required
def list_snippets(request):
    snippets = Snippet.objects.all().order_by("created_date")
    return render(request, "snippets/list_snippets.html", {"snippets": snippets})