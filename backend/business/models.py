from django.db import models
import uuid

class Category(models.Model):
    """
    Model to represent product categories.
    """
    # Unique identifier for each category
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key

    # Timestamp when the category was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp when the category was last modified
    modified_at = models.DateTimeField(auto_now=True)

    # Name of the category, max length 100 characters
    name = models.CharField(max_length=100)

    # Optional description of the category
    description = models.TextField(blank=True, null=True)

    # Optional image for the category
    image = models.ImageField(upload_to='category_image/', blank=True, null=True)

    def __str__(self):
        # Return the category name as the string representation
        return self.name

    class Meta:
        # Singular and plural names for the model
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Business(models.Model):
    """
    Model to represent a business entity.
    """
    # Unique identifier for each business
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Timestamp when the business was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp when the business was last modified
    modified_at = models.DateTimeField(auto_now=True)

    # Name of the business, max length 100 characters
    name = models.CharField(max_length=500)

    # Optional email of the business
    email = models.EmailField(max_length=100, blank=True, null=True)

    # Optional phone number of the business
    phone = models.CharField(max_length=15, blank=True, null=True)

    # ForeignKey to Country model (optional)
    country = models.ForeignKey('location.Country', on_delete=models.CASCADE, blank=True, null=True)

    # ForeignKey to City model (optional)
    city = models.ForeignKey('location.City', on_delete=models.CASCADE, blank=True, null=True)

    # ForeignKey to Street model (optional)
    street = models.ForeignKey('location.Street', on_delete=models.CASCADE, blank=True, null=True)

    # longitude of the business
    longitude = models.FloatField(blank=True, null=True)

    # latitude of the business
    latitude = models.FloatField(blank=True, null=True)

    # Optional ZIP code of the business
    zip = models.CharField(max_length=10, blank=True, null=True)

    # Optional website URL of the business
    website = models.URLField(max_length=100, blank=True, null=True)

    # Optional description of the business
    description = models.TextField(blank=True, null=True)

    # Optional logo image for the business
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)

    # Optional banner image for the business
    banner = models.ImageField(upload_to='business_banner/', blank=True, null=True)

    # Rating of the business
    rating = models.FloatField(default=0)
    # Status of the business (active or not)
    active = models.BooleanField(default=True)

    # Indicates if the business is verified
    verified = models.BooleanField(default=False)

    # Timestamp when the business was verified (optional)
    verified_on = models.DateTimeField(blank=True, null=True)

    # ForeignKey to User who verified the business (optional)
    verified_by = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True)

    # Status of business verification (optional)
    verified_status = models.CharField(max_length=10, blank=True, null=True)

    # Optional verification file for the business
    verified_file = models.FileField(upload_to='business_verified/', blank=True, null=True)

    # Many-to-many relationship with User model (business owners)
    owner = models.ManyToManyField('user.User', related_name='business_owner', blank=True)

    # Many-to-many relationship with Category model
    category = models.ManyToManyField('Category', related_name='business_category')

    def __str__(self):
        # Return the business name as the string representation
        return self.name

    class Meta:
        # Singular and plural names for the model
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'

class MyBusiness(models.Model):
    """
    Model to represent businesses associated with a user.
    """,
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Timestamp when the record was created
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # Timestamp when the record was last modified
    modified_at = models.DateTimeField(auto_now=True, null=True)

    # ForeignKey to Business model, with related_name to avoid clashes
    business = models.ForeignKey('Business', on_delete=models.CASCADE, related_name='user_businesses')

    # Many-to-many relationship with Business model, with related_name to avoid clashes
    associated_businesses = models.ManyToManyField('Business', related_name='associated_users')

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    def __str__(self):
        # Assuming you have a User model with an email field
        return f"{self.user.email} - {self.business.name}"


