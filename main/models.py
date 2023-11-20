from os.path import splitext

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()


def slugify_upload(instance, filename):
    folder = instance._meta.model_name
    name, ext = splitext(filename)
    name_t = slugify(name) or name
    return f"{folder}/{name_t}{ext}"


class Board(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=slugify_upload, blank=True, null=True)
    accessible = models.BooleanField(default=False)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Favourite(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
