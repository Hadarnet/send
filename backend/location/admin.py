from django.contrib import admin
from . import models

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Language model.
    """
    list_display = [
        'id',          # Unique identifier for the language
        'created_at',  # Timestamp when the record was created
        'modified_at', # Timestamp when the record was last modified
        'name'         # Name of the language
    ]
    
    search_fields = ['name']
    list_filter = ['created_at', 'modified_at']

@admin.register(models.Continent)
class ContinentAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Continent model.
    """
    list_display = [
        'id',          # Unique identifier for the continent
        'created_at',  # Timestamp when the record was created
        'modified_at', # Timestamp when the record was last modified
        'name',        # Name of the continent
        'longitude',   # Longitude of the continent's central point
        'latitude'     # Latitude of the continent's central point
    ]
    
    search_fields = ['name']
    list_filter = ['created_at', 'modified_at']

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Country model.
    """
    list_display = [
        'id',              # Unique identifier for the country
        'created_at',      # Timestamp when the record was created
        'modified_at',     # Timestamp when the record was last modified
        'name',            # Name of the country
        'population',      # Population of the country
        'latitude',        # Latitude of the country's central point
        'longitude',       # Longitude of the country's central point
        'flag',            # URL or path to the country's flag image
        'capital',         # Capital city of the country
        'get_continents'   # Custom method to display associated continents
    ]
    
    search_fields = ['name', 'population']
    list_filter = ['created_at', 'modified_at', 'continent', 'language']
    
    def get_continents(self, obj):
        """
        Returns a comma-separated list of continents associated with the country.
        """
        return ", ".join(continent.name for continent in obj.continent.all())
    get_continents.short_description = 'Continents'

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the City model.
    """
    list_display = [
        'id',          # Unique identifier for the city
        'created_at',  # Timestamp when the record was created
        'modified_at', # Timestamp when the record was last modified
        'name',        # Name of the city
        'latitude',    # Latitude of the city
        'longitude',   # Longitude of the city
        'country'      # Associated country of the city
    ]
    
    search_fields = ['name', 'country__name']
    list_filter = ['created_at', 'modified_at', 'country']

@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Street model.
    """
    list_display = [
        'id',          # Unique identifier for the street
        'created_at',  # Timestamp when the record was created
        'modified_at', # Timestamp when the record was last modified
        'name',        # Name of the street
        'city',        # Associated city of the street
        'longitude',   # Longitude of the street
        'latitude'     # Latitude of the street
    ]
    
    search_fields = ['name', 'city__name']
    list_filter = ['created_at', 'modified_at', 'city']
