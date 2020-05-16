from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    #надо ли и где пароль
    username = models.TextField(max_length=30)
    info = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(null= True, blank=True)

    def __str__(self):
        return f'{self.username}'

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=150)