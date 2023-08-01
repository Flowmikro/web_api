from django.urls import path

from .views import CustomUserAPIList, PostAPIList, PostCreateAPIList, PostDestroyAPILIst


urlpatterns = [
    path('', CustomUserAPIList.as_view()),
    path('user/post/<int:user_id>/', PostAPIList.as_view()),
    path('create/', PostCreateAPIList.as_view()),
    path('delete/<int:pk>/', PostDestroyAPILIst.as_view())
]