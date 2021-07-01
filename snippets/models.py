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
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="snippets")
    description = models.TextField()
    tags = models.ManyToManyField("Tags", related_name="snippets")
    created_date = models.DateTimeField(default=timezone.now)
    LANGUAGE_CHOICES = [
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('javascript', 'JavaScript'),
        ('bash', 'Bash'),
        ('cpp', 'C++'),
        ('django', 'Django'),
        ('git', 'Git'),
        ('http', 'HTTP'),
        ('gitignore', '.ignore'),
        ('json', 'JSON'),
        ('php', 'PHP'),
        ('python', 'Python'),
        ('jsx', 'React JSX'),
        ('regex', 'Regex'),
        ('rest', 'reST'),
        ('ruby', 'Ruby'),
        ('sql', 'SQL'),
    ]
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=25)
    copy_count = models.IntegerField()

    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)

    def __str__(self):
        return self.name
