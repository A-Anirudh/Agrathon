from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100,widget=forms.TextInput(attrs={'class':'textbox'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'textbox'}))

class NewUserForm(forms.Form):
    USER_TYPE_CHOICES = (
    (1, 'Farmer'),
    (2, 'Consumer'),
    )

    username = forms.CharField(label='Username', max_length=100,widget=forms.TextInput(
                              attrs={'class': "username"}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(
                              attrs={'class': "email"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':"password"}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':"phone_number"}))
    city = forms.CharField(widget=forms.TextInput(
                              attrs={'class': "username"}))
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES,widget=forms.Select(attrs={'class':"user_type"}))