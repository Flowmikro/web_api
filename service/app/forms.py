from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

    # выполняет автоматическое заполнение поле user
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # здесь мы извлекаем значение user из переданных аргументов kwargs
        super().__init__(*args, **kwargs)  # вызываем метод __init__ у родителя, чтобы выполнить инициализацию формы
        if self.user:
            self.initial['user'] = self.user  # позволяет автоматически предзаполнить это поле значением user

    # сохранения данных формы в модель
    def save(self, commit=True):
        instance = super().save(commit=False)  # получаем объект модели Post без сохранения его в базу
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance


class RegisterForm(UserCreationForm):
    """Форма для регистрации"""
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


# формы для CustomUser, так как CustomUser теперь вместо User
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')