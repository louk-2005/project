from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.utils import timezone

from home.models import Post


class Subscription(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='used_with')
    created = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} - {self.created}'


    def rest_of_time(self):
        total_duration = self.time * 24 * 60 * 60
        elapsed_time = (timezone.now() - self.created).total_seconds()
        remaining_time = total_duration - elapsed_time
        remaining_time = timedelta(seconds=remaining_time)
        return remaining_time

def is_subscribed(user):
    if Subscription.objects.filter(user=user).exists():
        return 1
    return 0

class MyFavorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='favorites')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='favorites')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return f'{self.user} - {self.post}'