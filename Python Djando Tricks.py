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
