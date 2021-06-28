from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, Tags, User
from django.utils import timezone
from .forms import SnippetForm

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

def snippet_details(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    add_snippet
    return render(request, "snippets/snippet_details.html", {"snippet": snippet})

def add_snippet(request):
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.save()
            return redirect("snippet_details", pk=snippet.pk)
    else:
        form = SnippetForm()

    return render(request, "snippets/add_snippet.html", {"form": form})

@login_required
def my_snippets(request):
    user = request.user
    snippets = Snippet.objects.filter(author=user)
    return render(request, "snippets/my_snippets.html", {"snippets": snippets})