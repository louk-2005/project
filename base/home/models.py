from django.db import models

from accounts.models import Subscription

class Topic(models.Model):
    topic = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    primary=models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return f'{self.topic}-{self.created}'

