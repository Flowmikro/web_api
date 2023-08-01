from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import login
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import CustomUser, Post
from .forms import PostForm, RegisterForm


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
        user = get_object_or_404(CustomUser, id=user_id)
        posts = Post.objects.filter(user=user)
        return Response({'user': user, 'posts': posts})


class UserAdd(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/user_add.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(login_required)  # Обернул методы get() и post() с помощью декоратора для проверки авторизации
    def get(self, request):
        form = PostForm()
        return Response({'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return Response({'form': form})


class PostDelete(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/delete_post.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(login_required)
    def delete(self, request, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id, user=request.user)
        post.delete()
        return redirect(reverse('user_posts', args=[request.user.id]))

    @method_decorator(login_required)
    def get(self, request, **kwargs):
        return self.delete(request, **kwargs)

    @method_decorator(login_required)
    def post(self, request, **kwargs):
        return self.delete(request, **kwargs)


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user_add')