from django import forms
from .models import Customer, Farmer

class AddToCartForm(forms.Form):
    qty = forms.IntegerField(required=True)

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class FarmerUpdateForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields =  "__all__"
