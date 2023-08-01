from django.urls import path

from .views import CustomUserAPIList, PostAPIList, PostCreateAPIList, PostDestroyAPILIst


urlpatterns = [
    path('', CustomUserAPIList.as_view()),  # http://127.0.0.1:8000/api/
    path('user/post/<int:user_id>/', PostAPIList.as_view()),  # http://127.0.0.1:8000/api/user/post/2/
    path('create/', PostCreateAPIList.as_view()),  # http://127.0.0.1:8000/api/create/
    path('delete/<int:pk>/', PostDestroyAPILIst.as_view())  # http://127.0.0.1:8000/api/delete/2/
]