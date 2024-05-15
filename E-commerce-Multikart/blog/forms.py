from typing import Any
from blog.models import Contact
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'firstName',
            'lastName',
            'number',
            'email',
            'message'
        )
        widgets = {
            'firstName' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Enter  Your  First  Name')
            }),
            'lastName' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' :_('Enter Your Last Name')
            }),
            'number' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Enter Your Number')
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Enter Your Email')
            }),
            'message' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Write Your Message'),
                'rows' : 6
            })
            
                 }
        
    def clean(self) -> dict[str, Any]:
        value = self.cleaned_data['email']
        if not value.endswith('gmail.com'):
             raise forms.ValidationError('Email must be gmail.com')   
        return super().clean()
    
    # def clean_firstName(self):
    #     value = self.cleaned_data['firstName']
    #     return value.upper()    