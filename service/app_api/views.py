from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView

from app.models import CustomUser, Post
from .serializers import CustomUserSerializers, PostSerializers


class CustomUserAPIList(ListAPIView):
    """API список поль-ей"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers


class PostAPIList(ListAPIView):
    """API список постов"""
    serializer_class = PostSerializers

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id=user_id)


class PostCreateAPIList(CreateAPIView):
    """API Создает новый пост"""
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDestroyAPILIst(RetrieveDestroyAPIView):
    """API Удаляет пост"""
    queryset = Post.objects.all()
    serializer_class = PostSerializers

