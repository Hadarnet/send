# Django Imports
from django.apps import AppConfig

class SettingsConfig(AppConfig):
    """
    Configuration for the Settings app.
    """
    
    # Default field type for auto-generated primary keys.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The full Python path to the application.
    name = 'settings'
