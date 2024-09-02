from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages

from .models import Topic, Post, LikePost, DislikePost, Comment
from accounts.models import Subscription
from accounts.models import is_subscribed

class HomeView(View):
    def get(self, request):
        can_see=0
        topics = Topic.objects.all()
        posts = Post.objects.all()
        if request.user.is_authenticated:
            can_see = is_subscribed(request.user)
        return render(request,'home/home.html',{'topics':topics,'posts':posts,'can_see':can_see})
class PricesView(View):
    def get(self, request):
        return render(request,'home/prices.html')

class TopicInfoView(View):
    def get(self, request,*args, **kwargs):
        can_see=0
        topic_info = Topic.objects.get(id=kwargs['topic_id'])
        posts = topic_info.posts.all()
        if request.user.is_authenticated:
            can_see = is_subscribed(request.user)
        return render(request, 'home/topic_info.html',{'topic_info':topic_info,'posts':posts,'can_see':can_see})
class PostView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'],slug=kwargs['post_slug'])
        comments = post.Pcomments.filter(is_reply=False)
        return render(request, 'home/post.html',{'post':post ,'comments':comments})
class LikeView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        like_post = LikePost.objects.filter(user=request.user, post=post)
        dislike_post = DislikePost.objects.filter(user=request.user, post=post)
        if like_post:
            messages.error(request,'You liked this post at last','danger')
        elif dislike_post:
            dislike_post.delete()
            LikePost.objects.create(user=request.user, post=post)
        else:
            LikePost.objects.create(user=request.user, post=post)
            messages.success(request,'You like this post successfully','success')
        return redirect('home:post', post.id,post.slug)
class DislikeView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        like_post = LikePost.objects.filter(user=request.user, post=post)
        dislike_post = DislikePost.objects.filter(user=request.user, post=post)
        if like_post :
            like_post.delete()
            DislikePost.objects.create(user=request.user, post=post)
        elif dislike_post :
            messages.error(request,'You disliked this post at last','danger')
        else:
            DislikePost.objects.create(user=request.user, post=post)
        return redirect('home:post', post.id, post.slug)



