from django import forms
from .models import Profiles


class PostForm(forms.ModelForm):
    class Meta:
        model = Profiles
        exclude = [""]
