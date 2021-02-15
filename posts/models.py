""" Posts models """

from django.db import models

# Para crear una tabla hay que make a class

class User(models.Model):
    """User model."""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.EmailField(max_length=100)
    last_name = models.EmailField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    
    # auto_now_add -> Ponga la fehca actual
    # auto_now -> Ponga la ULTIMA date que se actulizo
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return email"""
        return self.email
    