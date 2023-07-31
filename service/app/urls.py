from django.urls import path
from .views import UserList, UserPosts

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('user/<int:user_id>/posts/', UserPosts.as_view(), name='user_posts'),
]