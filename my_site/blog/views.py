from datetime import date

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


def get_date(post):
    return post['date']

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
        
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    order = ["-date"]
    context_object_name = "all_posts"


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    # selected_post = next(post for post in all_posts if post['slug'] == slug)

    # selected_post = []
    # for post in all_posts:
    #     if post["slug"] == slug:
    #         selected_post = post
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })