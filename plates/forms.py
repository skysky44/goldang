from django import forms

from .models import Post, Review, Comment, QuestionAndAnswer


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'restaurant_type',
            'loc',
            'image',
        )


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'rating',
            'visited_date',
        )


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = (
            'content',
        )



class QuestionAndAnswerForm(forms.ModelForm):
    
    class Meta:
        model = QuestionAndAnswer
        fields = (
            'title',
            'content',
        )
