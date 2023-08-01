from django.urls import path

from .views import CustomUserAPIList, PostAPIList, PostCreateAPIList, PostDestroyAPILIst


urlpatterns = [
    path('', CustomUserAPIList.as_view(), name='users_list'),  # http://127.0.0.1:8000/api/
    path('post/<int:user_id>/', PostAPIList.as_view(), name='posts_list'),  # http://127.0.0.1:8000/api/post/2/
    path('create/', PostCreateAPIList.as_view(), name='create_post'),  # http://127.0.0.1:8000/api/create/
    path('delete/<int:pk>/', PostDestroyAPILIst.as_view(), name='destroy_post')  # http://127.0.0.1:8000/api/delete/2/
]