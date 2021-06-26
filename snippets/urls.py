from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homepage, name="home"),
    path("list/", views.list_snippets, name='list_snippets'),
    path('accounts/', include('registration.backends.simple.urls')),
]