from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey

class Topic(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100,default='name')
    is_parent = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        return self.name

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    body = RichTextUploadingField()
    primary=models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return f'{self.topic}-{self.created}'
    def number_of_likes(self):
        return self.plikes.count()
    def number_of_dislikes(self):
        return self.dplikes.count()

class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ulikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='plikes')
    def __str__(self):
        return f'{self.user} like {self.post.slug}'
class DislikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dulikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dplikes')
    def __str__(self):
        return f'{self.user} dislike {self.post.slug}'
class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='Ucomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Pcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies',null=True, blank=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.post}-{self.body}'





