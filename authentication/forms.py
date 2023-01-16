from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class NewUserForm(forms.Form):
    USER_TYPE_CHOICES = (
    (1, 'Farmer'),
    (2, 'Consumer'),
    )

    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    phone_number = forms.IntegerField()
    city = forms.CharField()
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)