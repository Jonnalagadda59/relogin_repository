from django import forms
class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='Enter first name:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'first name',
                'class': 'from-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Enter last name:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'last name',
                'class': 'from-control'
            }
        )
    )
    username = forms.CharField(
        label='Enter username:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'from-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter password:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'from-control'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter mobile number:',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'mobile',
                'class': 'from-control'
            }
        )
    )
    email = forms.EmailField(
        label='Enter email:',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'email',
                'class': 'from-control'
            }
        )
    )




class LoginForm(forms.Form):
    username = forms.CharField(
        label='Enter username:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'from-control'
            }
        )
    )
    password = forms.CharField(
        label='Enter password:',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'from-control'
            }
        )
    )