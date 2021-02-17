from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Vamos heredar de auth model porque ya tiene metodos
# prestablecidos para crear un usuario
 
class Profile(models.Model):
    """ Profile model 
    
    Proxy model taht extends the base data with other
    information
    """

    # on delete especifica como se va a borrar los campos que estas
    # asociados

    # PROTECT Es imposible borrar este campo porque has fields asociate

    # Se puiede recibir un metodo too
    ## See Documentation

    # OneToOneField solo pudee haber un user con ese perfil
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    website = models.URLField(max_length=200,blank=True)
    
    biography = models.TextField(blank=True)
    
    phone_number = models.CharField(max_length=20,blank=True)
    
    # Se puede cuadrar la altura y el ancho HACE un resize }??
    # Instalat lib to this
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    
    create = models.DateTimeField(auto_now_add=True)
    
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return username."""
        return self.user.username


""" OJO POR CADA APP QUE CREE HAY QUE REGISTER IN SETTINGS.PY"""
""" OJO POR CADA APP QUE CREE HAY QUE REGISTER IN SETTINGS.PY"""
""" OJO POR CADA APP QUE CREE HAY QUE REGISTER IN SETTINGS.PY"""
""" OJO POR CADA APP QUE CREE HAY QUE REGISTER IN SETTINGS.PY"""