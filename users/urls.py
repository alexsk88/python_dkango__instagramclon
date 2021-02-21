"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

# Views
from users import views


urlpatterns = [

     #Posts Vista basada en clases
     #    view=TemplateView.as_view(template_name='users/detail.html'),
    path(
        route='/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

     #Managements
    path(
        route='/login/',
        view=views.login_view,
        name='login'),

    path(route='/logout/',
         view=views.logout_view,
         name='logout'),

    path(route='/signup/',
         view=views.signup,
         name='signup'),

    path(route='/me/profile/',
         view=views.update_profile,
         name='update_profile'),
]
