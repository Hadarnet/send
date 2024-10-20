
from django.contrib import admin
from .models import UserSettings

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserSettings model.
    """

    # Fields to display in the list view of the UserSettings model.
    list_display = ['id', 'user', 'dark_mode', 'notifications', 'language']

    # Fields to enable search functionality.
    search_fields = ['user__email', 'language']

    # Filters to add to the right sidebar in the list view.
    list_filter = ['dark_mode', 'notifications', 'language']
