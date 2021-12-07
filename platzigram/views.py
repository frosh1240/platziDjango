from json.encoder import JSONEncoder
from django.http.response import HttpResponse, JsonResponse
import json
from datetime import datetime

def helloWorld(request):
    now  = datetime.now().strftime('%b %dth,%Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time is {now}'.format(now =  now))


def hi(request):
    numbers = map(int, request.GET['numbers'].split(','))
    list_str = [number for number in numbers]
    list_str.sort()
    njson = JsonResponse(list_str, safe=False)
    return njson


def sorted(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_this = sorted(numbers)
    data = {
        'status: ': 'OK',
        'numbers: ': sorted_this,
        'message: ' : 'Integers sorted successfully' 
    }
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def sorted_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)