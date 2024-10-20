from django.apps import AppConfig

class BusinessConfig(AppConfig):
    """
    Configuration class for the 'business' app.
    """
    
    # Specify the default auto field type for models in this app.
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the app. This should match the app directory name.
    name = 'business'
