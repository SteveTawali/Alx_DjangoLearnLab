from django import forms
from .models import Post  # Ensure this is the correct model
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

# forms.py
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tag_names = [tag.strip() for tag in self.cleaned_data['tags'].split(',') if tag.strip()]
        tags = []
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        return tags
    
from django import forms
from .models import Post, Tag  # Ensure you import your models
from django.forms.widgets import TextInput, Textarea

# Example of a custom widget for tags
class TagWidget(forms.Select):
    # Define your custom widget behavior here
    pass  # Replace with the actual implementation or library you're using

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Ensure the 'tags' field exists in your model
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': Textarea(attrs={'placeholder': 'Write your content here'}),
            'tags': TagWidget(),  # This uses the custom TagWidget
        }

# Add any form logic or additional customization as needed