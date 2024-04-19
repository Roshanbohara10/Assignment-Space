# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager

# class CustomUSer(AbstractUser):
#     ROLE_CHOICES = [
#         ('ST', 'Student'),
#         ('ST', 'Teacher'),
#     ]
    
#     role = models.CharField(max_length=2, choices=ROLE_CHOICES)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email