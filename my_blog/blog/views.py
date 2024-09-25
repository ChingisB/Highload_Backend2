from django.shortcuts import render, get_object_or_404
from .custom_queries import get_post_with_comments
from .models import Post
from django.views.decorators.cache import cache_page


def get_post_by_id(request, post_id):
    post = get_object_or_404(get_post_with_comments(post_id))
    comments = post.comment_set.all()
    return render(request, 'post_with_comments.html', {'post': post, 'comments': comments})


@cache_page(60)
def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})