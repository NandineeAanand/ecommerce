from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
		
	shipping_full_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}), required=True)
	shipping_email=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}), required=True)
	shipping_address1=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Shipping Address 1'}), required=True)
	shipping_address2=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Shipping Address 2'}), required=True)
	shipping_city=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'City'}), required=True)
	shipping_state=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'State'}), required=False)
	shipping_country=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Country'}), required=True)
	shipping_zipcode=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Zipcode'}), required=False)
	class Meta:
		model = ShippingAddress 
		fields = ['shipping_full_name', 'shipping_address1','shipping_address2','shipping_city', 'shipping_state','shipping_zipcode','shipping_country']
		exclude=['user',]

class PaymentForm(forms.Form):
	card_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name on card'}), required=True)
	card_number=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Card Number'}), required=True)
	card_exp_name=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Expiration Date'}), required=True)
	card_cvv_number=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ' CVV Number'}), required=True)
	card_address1=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Address 1'}), required=True)
	card_address2=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Address 2'}), required=True)
	card_city=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing City'}), required=True)
	card_state=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing State'}), required=True)
	card_zipcode=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Zipcode'}), required=True)
	card_country=forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Billing Country'}), required=True)