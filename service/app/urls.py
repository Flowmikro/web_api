from django.urls import path
from .views import UserList, UserPosts, UserAdd, RegisterUser
from django.contrib.auth.views import LoginView, LogoutView

from . import views
urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('user/<int:user_id>/posts/', UserPosts.as_view(), name='user_posts'),
    path('user/posts_create/', UserAdd.as_view(), name='user_add'),

    path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]