from django.shortcuts import render
from .models import Todo
#from django.http import HttpResponse


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context={'todos':all})

def say_hello(request):
    person = {'name':'salman'}
    return render(request, 'hello.html', context=person)
