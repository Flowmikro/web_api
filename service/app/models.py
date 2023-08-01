from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):  # Копирую модель User, в нем уже есть поле email
    pass


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100)
    body = models.TextField('Текст')

    def __str__(self):
        return str(self.user)

