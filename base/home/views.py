from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Topic, Post, LikePost, DislikePost,Comment
from .forms import CommentForm,ReplyForm
from accounts.models import is_subscribed


class HomeView(View):
    def get(self, request):
        can_see=0
        topics = Topic.objects.filter()
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
        topic = Topic.objects.get(id=kwargs['topic_id'])
        posts = topic.posts.all()
        if request.user.is_authenticated:
            can_see = is_subscribed(request.user)
        return render(request, 'home/topic_info.html',{'topic':topic,'posts':posts,'can_see':can_see})
class PostView(View):
    form_class = CommentForm
    from_class_reply = ReplyForm
    def setup(self, request, *args, **kwargs):
        self.post_instance=Post.objects.get(id=kwargs['post_id'],slug=kwargs['post_slug'])
        return super().setup(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        post = self.post_instance
        comments = post.Pcomments.filter(is_reply=False)
        form = self.form_class()
        form_reply = self.from_class_reply()
        return render(request, 'home/post.html',{'post':post ,'comments':comments,'form':form,'form_reply':form_reply})
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.post_instance
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Your comment save successfully','success')
            return redirect('home:post', post.id, post.slug)
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
            messages.success(request, 'You like this post successfully', 'success')
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
            messages.success(request, 'You disliked this post successfully', 'success')
        elif dislike_post :
            messages.error(request,'You disliked this post at last','danger')
        else:
            DislikePost.objects.create(user=request.user, post=post)
            messages.success(request, 'You disliked this post successfully', 'success')
        return redirect('home:post', post.id, post.slug)
class ReplyView(View):
    form_class = ReplyForm
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        comment = Comment.objects.get(id=kwargs['comment_id'])
        form = self.form_class(request.POST)
        if form.is_valid():
            Reply = form.save(commit=False)
            Reply.user=request.user
            Reply.post = post
            Reply.reply = comment
            Reply.is_reply = True
            Reply.save()
            messages.success(request, 'Your reply save successfully','success')
            return redirect('home:post', post.id, post.slug)
        return redirect('home:post', post.id, post.slug)








