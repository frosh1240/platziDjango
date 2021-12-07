from django.http.response import HttpResponse
from django.shortcuts import render

#utilities 

from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1038',
    },
    {
        'name': 'Vía Láctea',
        'user': 'C. Vender',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1039',
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1020',
    }
]
# Create your views here.

def list_posts(request):

    content = []

    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure> <img src="{picture}"  /> </figure>
        """.format(**post))

    return HttpResponse('<br>'.join(content))