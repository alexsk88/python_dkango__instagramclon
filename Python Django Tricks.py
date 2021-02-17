python3 -m venv DIRECTORIO
apt-get install python3-venv
# Intalar varias versiones de python (algo como RVM)


source .env/bin/activate
# Activar el entorno virtual (se mete al folder e instala todas la librerias)

deactivate
# Desactiva entorno virtual


pip freeze
# Si deseamos ver las librerías instaladas en el ambiente

pip install django -U
# Instalacion de Django

django-admin
# ver la interfaz de Django

django-admin startproject platzigram .
# Crea un projecto de Django

python3 manage.py runserver
# Start project

import pdb; pdb.set_trace()
# Hacer un debbuger

python3 manage.py startapp NAMEHERE
# Crear una APP

python manage.py makemigrations
# Va a buscar los cambios en nuestros modelos y los va a reflejar en un archivo.

python manage.py migrate
# Va a aplicar esos cambios en nuestra base de datos.

python manage.py shell
# Abrir LA CONSOLA de Django.


    from posts.models import User # Important import the model !!
    b= User.objects.create(email='sashca@sashca.com',first_name='sashca',last_name='nova',password='sashca',is_admin=True)
    b.save()
    # Crear Un usuario desde la shell


    nova= User()
    nova.email='alex@alex.com'
    nova.first_name='Alex'
    nova.last_name='nova'
    nova.password='alex'
    nova.is_admin=False
    nova.save()
    # Otra manera de crear

    nova.delete()
    # Borrar un user


    User.objects.all()
    # Ver los objetos de la table

    User.objects.get(email="hermail@mail.com")
    # Buscar User -> como un find de rails

    User.objects.filter(email__endswith="hermail@mail.com")
    # Buscar con where, que terminen en %*algo*%

    from django.contrib.auth.models import User
    u = User.objects.create_user(username='yesika', password='admin123')
    # Crear un user con Django(ya viene configurado for more security)

python3 manage.py createsuperuser
# Crear un SUPERuser con Django(me pide user, mail, password)


