from .models import Post

def get_posts_with_comments():
    return Post.objects.prefetch_related('comment_set').all()