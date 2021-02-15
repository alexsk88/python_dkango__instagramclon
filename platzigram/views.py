"""Platzigram views."""

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime


def hello_world(request):
    """Return a greeting."""
    sacha = "Sacha"
    return HttpResponse('Oh, {sa}! Current server time is {now}'.format(sa="asjbdja",
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def hi(request):
    """Hi."""
    # El atributo request.META trae todos los headers de la peticion
    print("Resquest "+ str(request.META))
    # JUGAR CON LA CONSOLA
    # import pdb; pdb.set_trace()
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 14})

    # numbers = request.GET['numbers']
    # return HttpResponse(str(numbers))




#     """Platzigram views."""

# # Django
# from django.http import HttpResponse

# # Utilities
# from datetime import datetime
import json


def hello_world_2(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        # Este seria com JSON.parse
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def parametros(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)