from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from business.models import Business
import random
import string
from django.contrib.auth.models import Group
from business.models import Business
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

class UserManager(BaseUserManager):
    """
    Custom manager for User model with methods to create regular users and superusers.
    """
    def create_user(self, email, password=None, **kwargs):
        """
        Create and return a `User` with an email and password.
        """
        if email is None:
            raise TypeError("Users must have an email.")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError("Superusers must have a password.")
        if email is None:
            raise TypeError("Superusers must have an email.")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that includes additional fields and custom user manager.
    """
    # Primary key, auto-incrementing integer ID
    id = models.AutoField(primary_key=True)

    # Timestamp when the user was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp when the user was last modified
    modified_at = models.DateTimeField(auto_now=True)

    # User's first name
    first_name = models.CharField(max_length=255)

    # User's last name
    last_name = models.CharField(max_length=255)

    # Optional image field for a banner
    banner = models.ImageField(upload_to="user_banner/", blank=True, null=True)

    # Optional image field for profile picture
    pic = models.ImageField(upload_to="user_pic/", blank=True, null=True)

    # Optional field for user's date of birth
    birthday = models.DateField(null=True, blank=True)

    # User's email address, must be unique and indexed
    email = models.EmailField(db_index=True, unique=True)

    # Optional field for phone number
    phone = models.CharField(max_length=15, blank=True)

    # Optional field for Facebook profile URL
    facebook = models.URLField(blank=True)

    # Optional field for Twitter profile URL
    twitter = models.URLField(blank=True)

    # Optional field for Instagram profile URL
    instagram = models.URLField(blank=True)

    # Optional field for LinkedIn profile URL
    linkedin = models.URLField(blank=True)

    # Optional field for personal or business website URL
    website = models.URLField(blank=True)

    # Optional field for a user biography
    bio = models.TextField(blank=True)

    # Boolean field to determine if the user's email address has been verified
    is_verified = models.BooleanField(default=False)

    # Boolean field to determine if the user's account is active
    is_active = models.BooleanField(default=True)

    # Boolean field to determine if the user has staff permissions
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"  # Field used for authentication
    objects = UserManager()  # Custom manager for the User model

    def __str__(self):
        """
        Return the string representation of the User.
        """
        return self.email

    def get_businesses(self):
        """
        Return all businesses associated with the user through BusinessPermission.
        """
        return Business.objects.filter(businesspermission__user=self)

    class Meta:
        verbose_name = "User"  # Singular name for the model
        verbose_name_plural = "Users"  # Plural name for the model



class BusinessPermission(models.Model):
    """
    Model to manage permissions for users within specific businesses.
    """
    business = models.ForeignKey(Business, on_delete=models.CASCADE)  # Business associated with the permissions
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='business_permissions')  # User associated with the permissions
    permissions = models.ManyToManyField(Group, related_name='business_permissions')  # Permissions granted to the user for the business

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'business'], name='unique_user_business')
        ]
        verbose_name = 'Business Permission'  # Singular name for the model
        verbose_name_plural = 'Business Permissions'  # Plural name for the model

    def __str__(self):
        """
        Return a string representation of the BusinessPermission, listing permissions.
        """
        permissions_list = ", ".join([perm.name for perm in self.permissions.all()])
        return f"{self.user.email} - {self.business.name} - {permissions_list}"

    """
    Model to manage permissions for users within specific businesses.
    """
    # Business associated with the permissions
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    # User associated with the permissions
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='business_permissions')

    # Permissions granted to the user for the business
    permissions = models.ManyToManyField(Group, related_name='business_permissions')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'business'], name='unique_user_business')
        ]
        verbose_name = 'Business Permission'  # Singular name for the model
        verbose_name_plural = 'Business Permissions'  # Plural name for the model

    def __str__(self):
        """
        Return a string representation of the BusinessPermission, listing permissions.
        """
        permissions_list = ", ".join([perm.name for perm in self.permissions.all()])
        return f"{self.user.email} - {self.business.name} - {permissions_list}"




class Account(models.Model):
    """
    Model for accounts associated with users and businesses.
    """
    ACCOUNT_TYPES = (
        ('employee', 'Employee'),
        ('client', 'Client'),
        ('owner', 'Owner'),
    )

    id = models.AutoField(primary_key=True)  # Primary key, auto-incrementing integer ID
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the account was created
    modified_at = models.DateTimeField(auto_now=True)  # Timestamp when the account was last modified
    type = models.CharField(max_length=100, choices=ACCOUNT_TYPES)  # Type of the account
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')  # User associated with the account
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='accounts')  # Business associated with the account

    def __str__(self):
        """
        Return a string representation of the Account.
        """
        return f"{self.user.email} - {self.type} - {self.business.name}"



class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.otp_code}'
