from django import forms
from .models import Item
from .models import w_Item
from .models import Misc
from .models import Post

class currentBook(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'author', 'genre', 'description', 'day']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'day': forms.TextInput(attrs={'class': 'form-control'}),
        }

class wantBook(forms.ModelForm):
    class Meta:
        model = w_Item
        fields = ['name', 'author', 'genre', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class miscBook(forms.ModelForm):
    class Meta:
        model = Misc
        fields = ['name', 'author', 'genre', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }



class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
            }))

    class Meta:
        model = Post
        fields = ['body']