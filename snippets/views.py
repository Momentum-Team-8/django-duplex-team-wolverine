from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet, Tags, User
from django.utils import timezone
from .forms import SnippetForm
from django.contrib import messages

# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_snippets")
    else:
        return render(request, "snippets/home.html")

def list_snippets(request):
    snippets = Snippet.objects.all().order_by("created_date")
    return render(request, "snippets/list_snippets.html", {"snippets": snippets})

def snippet_details(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    add_snippet
    return render(request, "snippets/snippet_details.html", {"snippet": snippet})

def add_snippet(request):
    user = request.user.username
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
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

@login_required()
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

@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)

    if request.method == "POST":
        snippet.delete()
        messages.success(request, "Snippet deleted.")
        return redirect("list_snippets")

    return render(request, "snippets/delete_snippet.html", {"snippet": snippet})

def search_by_title(request):
    query = request.GET.get("q")
    results = Snippet.objects.filter(title__icontains=query)

    return render(request, "snippets/list_snippets.html", {"snippets": results})

def copy_snippet(request, pk):
    user = request.user
    snippet = get_object_or_404(klass=Snippet)