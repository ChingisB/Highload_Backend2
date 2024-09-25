from .models import Post

def get_post_with_comments(post_id):
    return Post.objects.prefetch_related('comment_set').get(id=post_id)