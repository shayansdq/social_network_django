from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Username', 'class': 'form-control'}
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter your email', 'class': 'form-control'}
        )
    )
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Enter your password', 'class': 'form-control'}
                                )
                                )
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Enter your password', 'class': 'form-control'}
                                )
                                )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email address is already exists!')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This username is already exists!')
        return username

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('Passwords is not match')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Username', 'class': 'form-control'}
    ))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Enter your password', 'class': 'form-control'}
                               )
                               )


class EditUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('age', 'bio')
