"""Posts views."""
from django.shortcuts import render, redirect
# Esta Linea es para exportar vistas HTML

# Create your views here.

# Django
from django.http import HttpResponse

# Decorador para auth
from django.contrib.auth.decorators import login_required

# Forms
from posts.forms import PostForm
# Models
from posts.models import Post

# Utilities
from datetime import datetime

# posts = [
#     {
#         'title': 'Mont Blanc',
#         'user': {
#             'name': 'Yésica Cortés',
#             'picture': 'https://picsum.photos/60/60/?image=1027'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/600?image=1036',
#     },
#     {
#         'title': 'Via Láctea',
#         'user': {
#             'name': 'Christian Van der Henst',
#             'picture': 'https://picsum.photos/60/60/?image=1005'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/800/800/?image=903',
#     },
#     {
#         'title': 'Nuevo auditorio',
#         'user': {
#             'name': 'Uriel (thespianartist)',
#             'picture': 'https://picsum.photos/60/60/?image=883'
#         },
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'photo': 'https://picsum.photos/500/700/?image=1076',
#     }
# ]

# posts_2 = [
#     {
#         'name': 'Mont Blac',
#         'user': 'Yésica Cortés',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=1036',
#     },
#     {
#         'name': 'Via Láctea',
#         'user': 'C. Vander',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=903',
#     },
#     {
#         'name': 'Nuevo auditorio',
#         'user': 'Thespianartist',
#         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
#         'picture': 'https://picsum.photos/200/200/?image=1076',
#     }
# ]


# def list_posts_test(request):
#     """List existing posts."""
#     content = []
#     for post in posts_2:
#         content.append("""
#             <p><strong>{name}</strong></p>
#             <p><small>{user} - <i>{timestamp}</i></small></p>
#             <figure><img src="{picture}"/></figure>
#         """.format(**post))

#         # En format tendria that set name=post['name'], user=post['user']
#         # para decirle que es name, ques es user y asi...
#         # para que python detecte esto con  **post el interpreta esas lineas
#     return HttpResponse('<br>'.join(content))

@login_required
def list_posts(request):
    """ List of posts with html render"""
    posts = Post.objects.all().order_by('-created')
    return render(request,'posts/feed.html',{'posts': posts})
    

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        # Traig los datos del usuario
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        # Pinte un form vacio
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
