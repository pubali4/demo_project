from django import forms

class SimpleForm(forms.Form):
	# name = forms.CharField(max_length = 20)
	# email = forms.EmailField(max_length = 40)
	# phno = forms.CharField(max_length = 12)
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'abc','placeholder':'enter your name'}
		),required=True,max_length=30)


	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'abc','placeholder':'enter your email id'}
		),required=True,max_length=30)
