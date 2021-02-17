""" User admin Clases"""

# Django

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile 

# Register your models here.
# Se puede registrar un modelo de varias maneras

#1 manera one
# admin.site.register(Profile)

#2 manera two con una clase

# porconvesion hay que add the word ADMIN
# Es lo mismo que arriba pero con una clase
# debe ser porque tiene que addd methods ??  jajaj:D i dont know
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile admin """
    
    # MOSTRAR COMPONENTES EXTRAs


    # Por lo general solo muestra el nombre en la view de profile
    # Si quiero that show more fields make a tuple
    # Se rompe si en la tupla coloco un valor que no exista !!!!
    # list_display = ('user', 'phone_number','website','peroo')
    list_display = ('user', 'phone_number','website','picture')

    # QUiere que al darle click me lleve a detalle , se lo tengo
    list_display_links = ('user',)

    # Se pueden editar directamente desde la tabla

    list_editable = ('phone_number', 'website', 'picture')

    # QUe campos quiere que se incluyan en la busquedas
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    # list_filter = (
    #     'created', NO SERVIA PORQUE SE ME FUE UNA d , quedo create
    #     'modified',
    #     'user__is_active',
    #     'user__is_staff',
    # )
    list_filter = (
        'user__is_active',
        'user__date_joined',
        'user__is_staff',
    )


# La manera en que muestra los "divs"
# Pueden ser en fila de dos tres etc
# Primero va el title despues los campos
# Si no queremos mostrar el titulo ponemos NONe

#   (None, {
#             'fields': ('url', 'title', 'content', 'sites')
#         }),

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields':(('modified','create'),),
        })
     
    )

    # Esto es obligatorio porque Django no puede modificar estos datos
    readonly_fields = ('create', 'modified',)

# PONER los campos para agregar Perfil de usuario en esta vista
class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)