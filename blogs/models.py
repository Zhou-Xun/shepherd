from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from taggit.managers import TaggableManager


class Author(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Study(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    file = models.FileField(upload_to='file/', null=True, blank=True)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_edit_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Life(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    file = models.FileField(upload_to='file/', null=True, blank=True)

    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_edit_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = RichTextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    life = models.ForeignKey(Life, on_delete=models.SET_NULL, null=True)
    study = models.ForeignKey(Study, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)