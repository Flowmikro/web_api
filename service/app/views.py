from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from .app_services import _delete_post, _select_user_post, _user_list_db
from .forms import PostForm, RegisterForm


def user_list(request):
    """Выводим список пользователей"""
    users = _user_list_db()
    return render(request, 'app/user_list.html', {'users': users})


def output_of_posts(request, user_id):
    """Выводим все посты пользователя"""
    data = _select_user_post(user_id)
    return render(request, 'app/user_posts.html', data)


@login_required(login_url='login')
def create_a_post(request):
    """Позволяет создавать посты только аутентифицированным поль-ям"""
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = PostForm()
    return render(request, 'app/user_add.html', {'form': form})


@login_required(login_url='login')
def post_delete(request, **kwargs):
    """Позволяет удалять посты только аутентифицированным поль-ям"""
    get_post_delete = _delete_post(request, **kwargs)
    return get_post_delete


class RegisterUser(CreateView):
    """Свой класс для регистрации, так как встроенный User переопределен"""
    form_class = RegisterForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user_add')
