from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import Post, Category

# Create your views here.
@require_GET
def index(request):
    posts = Post.objects.all().order_by("creation_date")
    categories = Category.objects.all()
    title = r"GreenMonkii"
    return render(request, "blog/index.html", {"posts": posts, "title": title, "categories": categories})