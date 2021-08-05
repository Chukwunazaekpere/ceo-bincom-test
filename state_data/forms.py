from django import forms
from django.db import models
from django.db.models import fields
from .models import (
    States
)

class AddStateForm(forms.ModelForm):
    class Meta:
        model = States
        fields = ["state_name"]