from typing import Any

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import Model
from rest_framework import serializers


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='media/avatar', blank=True)
    info = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='token')
    token = models.CharField(max_length=150)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'birth_date', 'password']
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def update(self, instance: Model, validated_data: Any):
        instance.username = validated_data.get('name', instance.username)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
