from django import forms
from django.contrib import admin
from django.http.request import HttpRequest

from django.contrib.auth.admin import  (
    UserAdmin 
)

from .models import (
    States,
    LGA,
    Ward,
    Party,
    PollngUnit
)

from .forms import (
    AddStateForm
)

@admin.register(States)
class StateAdmin(admin.ModelAdmin):
    list_display = ["state_id", "state_name"]
    prepopulated_fields = {"state_id": ["state_name"]}
    search_fields = ["state_name"]

    # forms = AddStateForm
    
    fieldsets = [
        ("None", {
            "fields": ["state_name", "state_id"]
        })
    ]


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = ["lga_name", "lga_id", "state", "lga_description", "date_entered"]
    search_fields = ["lga_name"]
    list_filter = ["lga_name"]
    prepopulated_fields = {"lga_id": ["lga_name"]}


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["party_name", "party_id"]
    search_fields = ["party_name"]
    list_filter = ["party_name"]
    prepopulated_fields = {"party_id": ["party_name"]}
    


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ["ward_name", "ward_id", "lga_id",]
    list_filter = ["lga_id"]
    search_fields = ["ward_name"]
    prepopulated_fields = {"ward_id": ["ward_name"]}
    autocomplete_fields = ["lga_id",]


@admin.register(PollngUnit)
class PollngUnitAdmin(admin.ModelAdmin):
    list_display = ["polling_unit_id", "ward_id", "lga_id", "polling_unit_number", "polling_unit_name", "polling_unit_description", "entered_by_user", "lattitude", "longitude", "date_entered"]
    search_fields = ["ward_name"]
    list_filter = ["polling_unit_name", "ward_id"]
    autocomplete_fields = ["lga_id", "ward_id", "entered_by_user"]