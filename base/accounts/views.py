from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in','warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'],email=cd['email'],password=cd['password'])
            messages.success(request,'You are now logged in','success')
            return redirect('home:home')
        return render(request,self.template_name,{'form':form})
class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in','warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'You are now logged in','success')
                return redirect('home:home')
            else:
                messages.error(request,' username or password is not correct','error')
        return render(request,self.template_name,{'form':form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request,'You are now logged out','success')
        return redirect('home:home')
