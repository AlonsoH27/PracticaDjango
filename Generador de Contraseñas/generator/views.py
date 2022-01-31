from django.shortcuts import render
from django.http import HttpResponse
import random 

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_pass = ''

    tamano = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!#$%&()*^'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    for x in range(tamano):
        generated_pass += random.choice(characters)

    return render(request, 'password.html', {'password': generated_pass})
