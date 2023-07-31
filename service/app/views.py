from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser, Post


class UserList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/user_list.html'

    def get(self, request):
        queryset = CustomUser.objects.all()
        return Response({'users': queryset})


class UserPosts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/user_posts.html'

    def get(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        posts = Post.objects.filter(user=user)
        return Response({'user': user, 'posts': posts})
