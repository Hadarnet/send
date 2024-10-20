from django.db import models

class Language(models.Model):
    # Unique identifier for each language instance
    id = models.AutoField(primary_key=True)
    
    # Timestamp for when the language record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the language record was last modified
    modified_at = models.DateTimeField(auto_now=True)
    
    # Name of the language
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Continent(models.Model):
    # Unique identifier for each continent instance
    id = models.AutoField(primary_key=True)
    
    # Timestamp for when the continent record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the continent record was last modified
    modified_at = models.DateTimeField(auto_now=True)
    
    # Name of the continent
    name = models.CharField(max_length=100)
    
    # Longitude of the continent's central point, optional
    longitude = models.FloatField(blank=True, null=True)
    
    # Latitude of the continent's central point, optional
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    # Unique identifier for each country instance
    id = models.AutoField(primary_key=True)
    
    # Timestamp for when the country record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the country record was last modified
    modified_at = models.DateTimeField(auto_now=True)
    
    # Name of the country
    name = models.CharField(max_length=100)
    
    # Population of the country, optional
    population = models.IntegerField(blank=True, null=True)
    
    # Latitude of the country's central point, optional
    latitude = models.FloatField(blank=True, null=True)
    
    # Longitude of the country's central point, optional
    longitude = models.FloatField(blank=True, null=True)
    
    # Many-to-many relationship with Language model, representing languages spoken in the country
    language = models.ManyToManyField('Language', related_name='countries_language', blank=True)
    
    # Path to the flag image of the country, optional
    flag = models.ImageField(upload_to='image/flags/', blank=True, null=True)
    
    # Capital city of the country, linked to the City model
    capital = models.OneToOneField('City', on_delete=models.CASCADE, related_name='countries_capital', blank=True, null=True)
    
    # Many-to-many relationship with Continent model, representing continents the country belongs to
    continent = models.ManyToManyField('Continent', related_name='countries_continent', blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    # Unique identifier for each city instance
    id = models.AutoField(primary_key=True)
    
    # Timestamp for when the city record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the city record was last modified
    modified_at = models.DateTimeField(auto_now=True)
    
    # Name of the city
    name = models.CharField(max_length=100)
    
    # Latitude of the city's central point, optional
    latitude = models.FloatField(blank=True, null=True)
    
    # Longitude of the city's central point, optional
    longitude = models.FloatField(blank=True, null=True)
    
    # Foreign key to Country model, representing the country the city belongs to
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities_country', blank=True, null=True)

    def __str__(self):
        return self.name
class Street(models.Model):
    # Unique identifier for each street instance
    id = models.AutoField(primary_key=True)
    
    # Timestamp for when the street record was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Timestamp for when the street record was last modified
    modified_at = models.DateTimeField(auto_now=True)
    
    # Name of the street, optional
    name = models.CharField(max_length=100, blank=True, null=True)
    
    # Foreign key to City model, representing the city where the street is located
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='streets_city', blank=True, null=True)
    
    # Longitude of the street, optional
    longitude = models.FloatField(blank=True, null=True)
    
    # Latitude of the street, optional
    latitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
