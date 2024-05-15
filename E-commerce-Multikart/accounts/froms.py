from django import forms
from typing import Any
from accounts.models import ShippingAdress
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):

    username = UsernameField(max_length=40, widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
            }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
            }))
    

class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',

            }))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('First  Name')
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Last Name')
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Username')
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Email')
            }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Password')
            }),

            
                 }
    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit)
        user.set_password(self.cleaned_data['password']) 
        user.is_active = False
        user.save()
        return user
    
    def clean(self) -> dict[str, Any]:
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Passwords must be same!')
        return super().clean()
    

class ShippingAdressForm(forms.ModelForm):

    class Meta:
        model = ShippingAdress
        fields = (
            'flat',
            'address',
            'zip_code',
            'country',
            'city',
            'region'
        )
        widgets = {
            'flat' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Company name')
            }),
            'address' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' :_('Address')
            }),
            'zip_code' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Zip_code')
            }),
            'country' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Country')
            }),
            'city' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('City'),
            }),
            'region' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : _('Region'),
            })
            
                 }
        

class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : _('Old Password')}
    ))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : _('New Password')}
    ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder' : _('Conform New Password')}
    ))


    class Meta:
        model = User
        fields=(
            'old_password',
            'new_password1',
            'new_password2'

        )


    