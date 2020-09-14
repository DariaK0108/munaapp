from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from .models import UserProfile, GENDER_CHOICES, EDU_CHOICES, INTEREST_CHOICES

class CustomRegisterForm(UserCreationForm):
    #email = forms.EmailField(required = False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address',required=False)
    age = forms.IntegerField(required=False)
    gender = forms.ChoiceField(label="Gender",initial='',widget=forms.Select(),required=False,choices=GENDER_CHOICES)
    education = forms.ChoiceField(label="Education level",initial='',widget=forms.Select(),required=False,choices=EDU_CHOICES)
    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=INTEREST_CHOICES,required=False)

    class Meta:
        model = UserProfile
        exclude = ['user']


