from django.contrib import admin

from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)

from django.contrib.auth.models import (
    Group
)
from .forms import (
    VotersRegistrationForm
)

from .models import Voters
# from django.contrib.auth 

@admin.register(Voters)
class VotersAdmin(BaseUserAdmin):
    list_display = ["firstname", "lastname", "email",  "phone", "polliing_unit_unique_id", "registration_date"]
    list_filter = ["polliing_unit_unique_id"] 
    search_fields = ["polliing_unit_unique_id"]
    add_form = VotersRegistrationForm

    fieldsets = [
        (None, {
            "fields": ["firstname", "lastname", "email", "phone", "password"]
        })
    ]

    add_fieldsets = [
        (None, {
            "fields": ["firstname", "lastname", "email", "phone", "password", "confirm_password", "polliing_unit_unique_id"]
        })
    ]

    filter_horizontal = []
    ordering = ["firstname"]

admin.site.unregister(Group)
admin.site.site_title  = "Bincom Dev"
admin.site.site_header  = "Bincom Dev"
