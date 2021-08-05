from django.contrib import admin


from .models import (
    ANNOUNCED_LGA_RESULTS,
    ANNOUNCED_PU_RESULTS,
    ANNOUNCED_WARD_RESULTS,
    ANNOUNCED_STATE_RESULTS
)


@admin.register(ANNOUNCED_STATE_RESULTS)
class StateResultsAdmin(admin.ModelAdmin):
    list_display = ["state_name", "party_abbreviation", "party_score", "entered_by_user", "date_entered", "user_ip_address"]
    autocomplete_fields = ["state_name", "party_abbreviation", "entered_by_user",]



@admin.register(ANNOUNCED_WARD_RESULTS)
class WardResultsAdmin(admin.ModelAdmin):
    list_display = ["ward_name", "party_abbreviation", "party_score", "entered_by_user", "date_entered", "user_ip_address"]
    autocomplete_fields = ["ward_name", "party_abbreviation", "entered_by_user",]



@admin.register(ANNOUNCED_PU_RESULTS)
class PUResultsAdmin(admin.ModelAdmin):
    list_display = ["lga_name", "party_abbreviation", "party_score", "entered_by_user", "date_entered", "user_ip_address"]
    autocomplete_fields = ["lga_name", "party_abbreviation", "entered_by_user",]


@admin.register(ANNOUNCED_LGA_RESULTS)
class LGAResultsAdmin(admin.ModelAdmin):
    list_display = ["lga_name", "party_abbreviation", "party_score", "entered_by_user", "date_entered", "user_ip_address"]
    autocomplete_fields = ["lga_name", "party_abbreviation", "entered_by_user",] 
    search_fields = ["lga_name"]
