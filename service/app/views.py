from django.shortcuts import redirect, render
from django.views.generic import CreateView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


from .models import CustomUser, Post
from .forms import PostForm


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


class UserAdd(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/user_add.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = PostForm()
        return Response({'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return Response({'form': form})


class RegisterUser(CreateView):
    ...
