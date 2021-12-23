from django import forms
from .models import Comments
import re

class NewComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'comment']
        labels = {
            'name': 'Name', 
            'comment': 'Text',
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Please enter your name'
            }),
            'comment':forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5,
                })
        }

