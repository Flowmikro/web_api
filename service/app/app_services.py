from django.shortcuts import redirect, reverse
from django.shortcuts import get_object_or_404

from .models import Post, CustomUser


def _select_user_post(user_id):
    """Выводит посты конкретного пользователя"""
    user = get_object_or_404(CustomUser, id=user_id)
    posts = Post.objects.filter(user=user)
    return {'user': user, 'posts': posts}


def _delete_post(request, **kwargs):
    """Удаляем пост конкретного пользователя"""
    post_id = kwargs.get('post_id')
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect(reverse('user_posts', args=[request.user.id]))