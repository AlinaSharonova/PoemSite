# Create your models here.

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Poem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)
    day = models.PositiveSmallIntegerField(blank=True, null=True)
    month = models.PositiveSmallIntegerField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    CATEGORIES_FOR_POEMS = (
         ('SAD', 'Sadness'),
         ('LOVE', 'Love'),
         ('OTHER', 'Other')
    )
    category = models.CharField(max_length=40, choices=CATEGORIES_FOR_POEMS)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CommentPoem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Пользователь", on_delete=models.CASCADE)
    title_poem = models.ForeignKey(Poem, verbose_name="Название стихотворения", on_delete=models.CASCADE)
    text = models.TextField("Текст комментария", max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return self.title_poem
