from django import forms

class AddToCartForm(forms.Form):
    qty = forms.IntegerField(required=True)