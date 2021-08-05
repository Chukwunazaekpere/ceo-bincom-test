from django import forms
from django.db import models
from django.db.models import fields
from .models import (
    Voters
)

class VotersRegistrationForm(forms.ModelForm):
    class Meta:
        model = Voters
        fields = "__all__"

    def save(self, commit=True):
        new_voter = super().save(commit=False)
        cleaned_data = self.cleaned_data
        print("\n\t Form: ", self.cleaned_data)
        new_voter.set_password(cleaned_data["password"])

        if commit:
            new_voter.save()
        return new_voter
