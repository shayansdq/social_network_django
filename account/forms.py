from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder':'Enter your Username','class':'form-control'}
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder':'Enter your email','class':'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'Enter your password','class':'form-control'}
        )
    )
