from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    language = models.CharField(max_length=100)
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="snippets")
    description = models.TextField()
    tags = models.ManyToManyField("Tags", related_name="snippets")
    created_date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)

    def __str__(self):
        return self.name
