# Django Imports
from django.apps import AppConfig

# User App Config
class UserConfig(AppConfig):
    """
    Configuration class for the 'user' application.
    This class is used to configure the 'user' app within the Django project.
    """
    
    # The default field type for primary keys (ID fields) in models for this app.
    default_auto_field = "django.db.models.BigAutoField"
    
    # The name of the application. This is used by Django to identify the app.
    name = "user"
    
    # An optional label for the app, useful for specifying app labels in certain contexts.
    label = "user"
