from django.db import models
from datetime import datetime as dt
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=1024, blank=False)
    post = models.TextField(blank=False)
    slug = models.SlugField(unique=True)
    image_url = models.URLField(blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="posts")

    def __str__(self) -> str:
        date = self.creation_date.strftime("%Y-%m-%d")
        return f"{self.slug} - {date}"