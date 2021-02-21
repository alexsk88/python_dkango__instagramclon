"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    # view=views.list_posts,
    # Pasa a ser un list view de Django
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.create_post,
        name='create_post'
    ),
  ]
