from typing import Any
from core.models import ProductComment
from django import forms
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
   

    class Meta:
        model = ProductComment
        fields = (
            'rating',
            'message',
        )
        widgets = {
            'message' : forms.TextInput(attrs={

                'class' : 'form-control',
                'placeholder' : _('Write Your Message'),
                'rows' : 6,
                
            })
            
                 }