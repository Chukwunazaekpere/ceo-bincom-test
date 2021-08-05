from django import forms
from django.db import models
from django.db.models import fields
from .models import (
    Voters
)

class VotersRegistration(forms.ModelForm):
    class Meta:
        model = Voters
        fields = "__all__"

    def save(self, commit=True):
        new_voter = super().save(commit=False)
        return new_voter
