from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import VitalSign

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VitalSignForm(forms.ModelForm):
    class Meta:
        model = VitalSign
        fields = ['blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate', 'temperature']
