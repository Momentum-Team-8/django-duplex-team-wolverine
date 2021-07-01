from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.list_snippets, name="home"),
    path("list/", views.list_snippets, name='list_snippets'),
    path('accounts/', include('registration.backends.simple.urls')),
    path("snippets/<int:pk>", views.snippet_details, name="snippet_details"),
    path("snippets/my_snippets", views.my_snippets, name="my_snippets"),
    path("snippets/new", views.add_snippet, name="add_snippet"),
    path("snippets/<int:pk>/edit", views.edit_snippet, name="edit_snippet"),
    path("snippets/<int:pk>/delete", views.delete_snippet, name="delete_snippet"),
    path("search", views.search_by_title, name="search_snippet"),
    path("snippets/<int:pk>copy", views.copy_snippet, name="copy_snippet")
]