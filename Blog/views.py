from django.shortcuts import render
from django.views.decorators.http import require_GET
from .models import Post, Category

# Create your views here.


@require_GET
def index(request):
    category = request.GET.get("cg")
    print(category)
    categories = Category.objects.all()
    posts = Post.objects.all().order_by("creation_date") if not category else categories.get(
        name=category).posts.order_by("creation_date")
    title = r"GreenMonkii"
    return render(request, "blog/index.html", {"posts": posts, "title": title, "categories": categories, "cg": category})
