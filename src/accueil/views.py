from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def article(request, num_article):
    if num_article not in ['01', '02', '03']:
        return render(request,f"home/article_not_found.html")
    return render(request,f"home/article{num_article}.html")