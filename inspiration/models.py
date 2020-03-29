# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Poem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=200)
    text = models.TextField()
    day = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
    month = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
    year = models.PositiveSmallIntegerField(max_length=4, blank=True, null=True)
    published_date = models.DateTimeField()
    CATEGORIES_FOR_POEMS = (
        ('SAD', 'Sadness'),
        ('LOVE', 'Love'),
        ('OTHER', 'Other')
    )
    categories = models.CharField(max_length=40, choices= CATEGORIES_FOR_POEMS)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
