from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):    
    return render(request, 'DjangoGrip/index.html', context={'name': 'Yanis', 'age': '19', 'date': datetime.now()})