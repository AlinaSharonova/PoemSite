from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/avatar', blank=True)
    info = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=150)