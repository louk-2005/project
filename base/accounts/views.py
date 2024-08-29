from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import LoginForm

class RegisterView(View):
    form_class = LoginForm
    template_name = 'accounts/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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
    pass