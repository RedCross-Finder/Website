from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

currentYear = datetime.now().year

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, int(currentYear))), required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'password1', 'password2']