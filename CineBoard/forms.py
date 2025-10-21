from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'release_date', 'rating', 'tags', 'poster']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Напишите комментарий...'})
        }