from .models import Comments, Order
from django.forms import ModelForm, TextInput
from django import forms

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


class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date' }))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )