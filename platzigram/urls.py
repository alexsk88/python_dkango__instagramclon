"""platzigram URL Configuration
 QUE ES ADMIN ?? Es para acceder al menu de admins como wordpress"""
from django.contrib import admin

# Para ver la imagenes
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [

    path('admin/', admin.site.urls),

    path('posts', include(('posts.urls', 'posts'), namespace='posts')),
    path('users', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

