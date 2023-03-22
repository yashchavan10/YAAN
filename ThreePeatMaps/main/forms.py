from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from .models import PastDetail


class PastForm(forms.ModelForm):
	
	start_address = forms.CharField(max_length=120, required=True, widget = forms.HiddenInput())
	end_address = forms.CharField(max_length=130, required=True, widget = forms.HiddenInput())

	class Meta:
		model = PastDetail
		fields = ('start_address','end_address')

