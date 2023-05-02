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
            'content',
            'rating',
            'taste_evaluation',
            'image',
        )
        widgets = {
            'content': forms.Textarea(attrs={
                'id': 'ReviewWriting__Main__Text',
                'class': 'ReviewWriting__Main__Text',
                'placeholder': '주문하신 메뉴는 어떠셨나요? 식당의 분위기와 서비스도 궁금해요!',
                'onkeyup': 'TextLength(this)',
                'onkeydown': 'TextLength(this)',
            })
        }


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
