from django import forms
from django.db import models
from django.db.models import fields
from .models import (
    Voters
)

class VotersRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=30)
    class Meta:
        model = Voters
        fields = ["firstname", "lastname", "email", "phone", "password", "confirm_password", "polliing_unit_unique_id"]
    
    def clean_confirm_password(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data["password"]
        confirm_password = cleaned_data["confirm_password"]

        if not confirm_password:
            raise forms.ValidationError("Enter the same input in the password field")
        elif password != confirm_password:
            raise forms.ValidationError("Both password fields must be same")
        return password

    def save(self, commit=True):
        new_voter = super().save(commit=False)
        cleaned_data = self.cleaned_data
        new_voter.set_password(cleaned_data["password"])
        if commit:
            new_voter.save()
        return new_voter
