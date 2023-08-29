from django import forms

class AuthenticateForm(forms.Form):
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password=forms.CharField(max_length=15, min_length=8, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    confirmation=forms.CharField(max_length=15, min_length=8, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))