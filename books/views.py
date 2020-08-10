from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# k = []


def index(request):
    return render(request, 'index.html')
    # with open('data.txt', 'r') as reader:
    #      k = (reader.read())
    #     print(k)


#    books = Books.objects.all()
#   render(request, 'index.html', {'books': books})
#  return HttpResponse(k)

def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})
