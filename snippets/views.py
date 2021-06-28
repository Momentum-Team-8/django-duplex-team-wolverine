from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, Tags
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


def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "GET":
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect("list_snippets")

    return render(request, "snippets/edit_snippet.html", {"form": form, "snippet": snippet})