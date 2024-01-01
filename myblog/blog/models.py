from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User


class PabMan(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField("max_length=250")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Посты')
    text = models.TextField()
    publ = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()  # Менеджер моделей по умолчанию
    published = PabMan()  # Менеджер моделей опубликованных постов

    class Meta:
        ordering = ['-publ']
        indexes = [
            models.Index(fields=['-publ']),
        ]

    def __str__(self):
        return self.title
