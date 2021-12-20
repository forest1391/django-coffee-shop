from django.http import HttpResponse
from django.shortcuts import render
from coffees.models import Coffee


# Create your views here.


def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})
