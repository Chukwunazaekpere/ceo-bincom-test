from django.contrib import admin

from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin
)

from django.contrib.auth.models import (
    Group
)

from .models import Voters
# from django.contrib.auth 

@admin.register(Voters)
class VotersAdmin(BaseUserAdmin):
    list_display = ["firstname", "lastname"]
    list_filter = ["polliing_unit_unique_id"] 
    search_fields = ["polliing_unit_unique_id"]
    

    fieldsets = [
        (None, {
            "fields": ["firstname", "lastname"]
        })
    ]

    add_fieldsets = [
        (None, {
            "fields": ["firstname", "lastname"]
        })
    ]

    filter_horizontal = []
    ordering = ["firstname"]

admin.site.unregister(Group)
admin.site.site_title  = "Bincom Dev"
admin.site.site_header  = "Bincom Dev"
