from .models import Comments
from django.forms import ModelForm, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'item_id', 'user_id']
        widgets = { 'text': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Напиши мнение",
            'name': "TextComment",
            'id': "TextComment"
            })
        }