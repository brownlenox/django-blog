from django import forms
from .models import Article

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'featured']
