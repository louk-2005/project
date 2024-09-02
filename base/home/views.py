from django.shortcuts import render,redirect
from django.views import View

from .models import Topic, Post
from accounts.models import Subscription

class HomeView(View):
    def get(self, request):
        can_see=0
        topics = Topic.objects.all()
        posts = Post.objects.all()
        if request.user.is_authenticated:
            can_see = Subscription.objects.filter(user=request.user).exists()

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
            can_see = Subscription.objects.filter(user=request.user).exists()
        return render(request, 'home/topic_info.html',{'topic_info':topic_info,'posts':posts,'can_see':can_see})
class PostView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'],slug=kwargs['post_slug'])
        return render(request, 'home/post.html',{'post':post})
