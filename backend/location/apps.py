from django.apps import AppConfig

class LocationConfig(AppConfig):
    """
    Configuration for the Location app.
    """
    # Default auto field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    # Full Python path to the app
    name = 'location'

    # Optional: Human-readable name for the app
    verbose_name = "Location Management"

    def ready(self):
        """
        Override this method to run code when the app is ready.
        This is a good place to import signal handlers or perform setup.
        """
        # Import signals or other initialization code here
        pass
