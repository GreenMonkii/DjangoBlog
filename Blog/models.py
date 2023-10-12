from django.db import models
from datetime import datetime as dt
from django.core.validators import RegexValidator
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Writer(models.Model):
    first_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="first name")
    last_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="last name")
    username = models.CharField(max_length=255, blank=False, unique=True, null=False,
                                help_text="Your username should only contain alphabets, numbers and underscores (-)",
                                validators=[RegexValidator(r"^[\w\d-]{5,}")])
    join_date = models.DateTimeField(auto_now=True)
    display_picture = models.ImageField(null=True, upload_to="user-img", blank=True)

    def __str__(self) -> str:
        return self.username
    

class Post(models.Model):
    title = models.CharField(max_length=1024, blank=False)
    post = models.TextField(blank=False)
    slug = models.SlugField(unique=True)
    writer = models.ForeignKey(to=Writer, on_delete=models.PROTECT, null=True, related_name="Posts")
    image_url = models.URLField(blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="posts")

    def __str__(self) -> str:
        date = self.creation_date.strftime("%Y-%m-%d")
        return f"{self.slug} - {date}"
