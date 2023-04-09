from django.forms import ModelForm
from django import forms
from django.db import models


class User(forms.ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User
        exclude = ('name',)


class User2(ModelForm):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        model = User2
        exclude = ('name',)
