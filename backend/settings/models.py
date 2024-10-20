# Django Imports
from django.db import models
from django.contrib.auth.models import Group, Permission, BaseUserManager

class UserSettingsManager(BaseUserManager):
    """
    Manager for creating and managing UserSettings instances.
    """
    
    def create_settings(self, user, **kwargs):
        """
        Create and return a UserSettings instance for the given user.
        
        :param user: The user to associate with the settings.
        :param kwargs: Additional keyword arguments.
        :return: The created UserSettings instance.
        """
        settings = self.model(user=user)
        settings.dark_mode = False  # Default setting for dark mode
        settings.notifications = True  # Default setting for notifications
        settings.save(using=self._db)
        return settings


class UserSettings(models.Model):
    """
    Model to store settings for a user, such as preferences for dark mode and notifications.
    """
    
    # User associated with these settings
    user = models.OneToOneField(
        'user.User', 
        on_delete=models.CASCADE, 
        related_name='user_settings'
    )
    
    # Indicates whether dark mode is enabled
    dark_mode = models.BooleanField(default=False)
    
    # Indicates whether notifications are enabled
    notifications = models.BooleanField(default=True)
    
    # Preferred language setting, optional
    language = models.CharField(max_length=20, blank=True)

    # Groups associated with the user settings
    groups = models.ManyToManyField(
        Group, 
        related_name='user_settings_groups', 
        blank=True
    )
    
    # Permissions associated with the user settings
    user_permissions = models.ManyToManyField(
        Permission, 
        related_name='user_settings_permissions', 
        blank=True
    )

    def __str__(self):
        """
        String representation of the UserSettings instance.
        
        :return: A string representing the user's settings.
        """
        return f"{self.user.first_name}'s settings"
