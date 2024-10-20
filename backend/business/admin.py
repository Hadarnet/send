# Django Imports
from django.contrib import admin
from .models import Business, Category, MyBusiness
from user.models import BusinessPermission

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Category model.
    """
    # Display these fields in the list view of the Category model
    list_display = (
        'id',                  # Unique identifier for the category
        'name',                # Name of the category
        'description',         # Description of the category
        'created_at',          # Timestamp when the record was created
        'modified_at'          # Timestamp when the record was last modified
    )
    
    # Add search functionality for these fields
    search_fields = (
        'name',                # Search by category name
        'description'          # Search by category description
    )
    
    # Add filters for these fields
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at'          # Filter by modification timestamp
    )
    
    # Optional: Default ordering by name
    ordering = ['name']

class UserBusinessPermissionInline(admin.TabularInline):
    """
    Inline form for UserBusinessPermission within the Business admin view.
    """
    model = BusinessPermission
    extra = 1  # Number of empty forms to display in the inline

    # Optional: Specify which fields to display in the inline form
    # fields = ['user', 'permission']

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Business model.
    """
    # Display these fields in the list view of the Business model
    list_display = (
        'id',                  # Unique identifier for the business
        'created_at',          # Timestamp when the record was created
        'modified_at',         # Timestamp when the record was last modified
        'name',                # Name of the business
        'email',               # Email address of the business
        'phone',               # Phone number of the business
        'country',             # Country where the business is located
        'city',                # City where the business is located
        'street',              # Street address of the business
        'zip',                 # ZIP code of the business location
        'website',             # Website URL of the business
        'description',         # Description of the business
        'logo',                # Logo image of the business
        'banner',              # Banner image of the business
        'active',              # Active status of the business
        'verified',   # Verification status of the business
        'verified_on', # Timestamp when the business was verified
        'verified_by', # User who verified the business
        'verified_status', # Status of the business verification
        'verified_file'   # File associated with the business verification
    )
    
    # Add search functionality for these fields
    search_fields = (
        'name',                # Search by business name
        'email',               # Search by business email
        'phone'                # Search by business phone number
    )
    
    # Add filters for these fields
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
        'active',              # Filter by active status
        'verified',   # Filter by business verification status
        'country',             # Filter by country
        'city',                # Filter by city
        'street'               # Filter by street
    )
    
    # Add inline form for UserBusinessPermission in the Business admin view
    inlines = [UserBusinessPermissionInline]

    # Optional: Default ordering by name
    ordering = ['name']

@admin.register(MyBusiness)
class MyBusinessAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the MyBusiness model.
    """
    # Display these fields in the list view of the MyBusiness model
    list_display = (
        'id',                  # Unique identifier for the MyBusiness record
        'modified_at',         # Timestamp when the record was last modified
        'business',            # Associated business
        'user'                 # Associated user
    )
    
    # Add search functionality for these fields
    search_fields = (
        'business__name',      # Search by associated business name
        'user__username'       # Search by associated user username
    )
    
    # Add filters for these fields
    list_filter = (
        'created_at',          # Filter by creation timestamp
        'modified_at',         # Filter by modification timestamp
    )
    
    # Optional: Default ordering by id
    ordering = ['id']
