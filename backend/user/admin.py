# Django Imports
from django.contrib import admin
from .models import User, Account, BusinessPermission, OTP

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.
    """

    # Fields to display in the list view of the User model.
    list_display = ['id', 'created_at', 'modified_at', 'first_name', 'last_name', 'email', 'phone', 'birthday', 'is_verified', 'is_active', 'is_staff']

    # Fields to enable search functionality.
    search_fields = ['email', 'first_name', 'last_name', 'phone']

    # Filters to add to the right sidebar in the list view.
    list_filter = ['created_at', 'modified_at', 'is_active', 'is_staff']

    # Fields that should be read-only.
    readonly_fields = ['created_at', 'modified_at']

    # Default ordering of objects in the list view.
    ordering = ['-created_at']

    # Number of objects to display per page in the list view.
    list_per_page = 20

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Account model.
    """

    # Fields to display in the list view of the Account model.
    list_display = ['id', 'created_at', 'modified_at', 'type', 'user', 'business']

    # Fields to enable search functionality.
    search_fields = ['user__email', 'type']

    # Filters to add to the right sidebar in the list view.
    list_filter = ['created_at', 'modified_at', 'type', 'business']

    # Fields that should be read-only.
    readonly_fields = ['created_at', 'modified_at']

    # Default ordering of objects in the list view.
    ordering = ['-created_at']

    # Number of objects to display per page in the list view.
    list_per_page = 20

@admin.register(BusinessPermission)
class BusinessPermissionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the BusinessPermission model.
    """

    # Fields to display in the list view of the BusinessPermission model.
    list_display = ['user_email', 'business', 'get_permissions']

    # Fields to enable search functionality.
    search_fields = ['user__email', 'business__name']

    # Filters to add to the right sidebar in the list view.
    list_filter = ['user', 'business']

    # Fields that should be read-only.
    readonly_fields = []  # Update this list if needed to enforce readonly fields

    # Default ordering of objects in the list view.
    ordering = ['user', 'business']

    # Number of objects to display per page in the list view.
    list_per_page = 20

    def user_email(self, obj):
        """
        Display the email of the user associated with the BusinessPermission.
        """
        return obj.user.email
    user_email.short_description = 'User Email'

    def get_permissions(self, obj):
        """
        Display a comma-separated list of permissions associated with the BusinessPermission.
        """
        return ", ".join([perm.name for perm in obj.permissions.all()])
    get_permissions.short_description = 'Permissions'

    def get_readonly_fields(self, request, obj=None):
        """
        Customize the readonly fields based on the object state (new or existing).
        """
        if obj:  # Editing existing objects
            return []  # Remove readonly fields if you need to allow edits
        return super().get_readonly_fields(request, obj)

    def save_model(self, request, obj, form, change):
        """
        Override save_model if additional logic is needed during save.
        """
        super().save_model(request, obj, form, change)

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    """
    Admin configuration for the OTP model.
    """
    # Fields to display in the list view of the OTP model.
    list_display = ['id', 'created_at', 'modified_at', 'user', 'otp_code']
    # Fields to enable search functionality.
    search_fields = ['user__email', 'otp_code']
    # Filters to add to the right sidebar in the list view.
    list_filter = ['created_at', 'modified_at']
    # Fields that should be read-only.
    readonly_fields = ['created_at', 'modified_at']
    # Default ordering of objects in the list view.
    ordering = ['-created_at']
    # Number of objects to display per page in the list view.
    list_per_page = 20