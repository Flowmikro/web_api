from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),  # http://127.0.0.1:8000/
    path('user/<int:user_id>/posts/', UserPosts.as_view(), name='user_posts'),  # http://127.0.0.1:8000/user/1/posts/
    path('user/posts_create/', UserAdd.as_view(), name='user_add'),  # http://127.0.0.1:8000/user/posts_create/
    path('delete/<int:post_id>/', PostDelete.as_view(), name='delete_post'),  # http://127.0.0.1:8000/delete/24

    path('register/', RegisterUser.as_view(), name='register'),  # http://127.0.0.1:8000/register/
    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),  # http://127.0.0.1:8000/login/
    path('logout/', LogoutView.as_view(), name='logout'),  # http://127.0.0.1:8000/logout/
]
