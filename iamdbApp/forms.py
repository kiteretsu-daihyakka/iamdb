from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=AuthUser
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']