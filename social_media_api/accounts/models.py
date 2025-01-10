from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # A field for user bio
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # A field for profile pictures
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following', 
        blank=True
    )  # Many-to-Many relationship for followers

    # Default fields for groups and permissions
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
    )

class Follow(models.Model):
    follower = models.ForeignKey(
        CustomUser, related_name="following_set", on_delete=models.CASCADE
    )
    followee = models.ForeignKey(
        CustomUser, related_name="followed_set", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "followee")  # Prevent duplicate relationships