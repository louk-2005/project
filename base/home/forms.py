from django import forms

from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
       # widgets ={
        #    'body': forms.Textarea(attrs={'class': 'form-control'}),
        #}
        labels ={
            'body': 'Comment'
        }
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
       # widgets ={
       #     'body': forms.Textarea(attrs={'class': 'form-control'}),
       # }
        labels ={
            'body': 'Reply',
        }
class ImageForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    image = forms.ImageField()

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))