from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Копирую модель User"""
    pass


class Post(models.Model):
    """Модель для добавления постов"""
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100)
    body = models.TextField('Текст')

    def __str__(self):
        return str(self.user)

