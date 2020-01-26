from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    # password1 = forms.CharField(label='re-type password', required=True, widget=forms.PasswordInput())
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','Profile_Picture')
