from django.shortcuts import render
#from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def say_hello(request):
    person = {'name':'salman'}
    return render(request, 'hello.html', context=person)
