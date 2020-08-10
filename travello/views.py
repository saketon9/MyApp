from django.shortcuts import render
from .models import destinations


# Create your views here.
def index(request):
    dest1 = destinations()
    dest1.name = 'Mumbai'
    dest1.desc = 'city never sleeps'
    dest1.price = 800
    dest1.img = 'destination_1.jpg'

    dest2 = destinations()
    dest2.name = 'Bangalore'
    dest2.desc = 'city very costly'
    dest2.price = 300

    dest3 = destinations()
    dest3.name = 'Delhi'
    dest3.desc = 'city with pollution'
    dest3.price = 800
    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})
