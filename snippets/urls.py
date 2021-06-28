from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homepage, name="home"),
    path("list/", views.list_snippets, name='list_snippets'),
    path('accounts/', include('registration.backends.simple.urls')),
    path("snippets/<int:pk>", views.snippet_details, name="snippet_details"),
    path("snippets/new", views.add_snippet, name="add_snippet"),
    path("snippets/<int:pk>/edit", views.edit_snippet, name="edit_snippet"),
    path("snippet/<int:pk>/delete", views.delete_snippet, name="delete_snippet"),
]