from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == "POST":
        res = requests.get("http://127.0.0.1:8080/todo/posts/", params = request.POST)
    
    else:
        res = requests.get("http://127.0.0.1:8080/todo/posts/",params = request.GET)
    
    if res.status_code == 200:
        datas = json.loads(res.content)
        return render(request, "index.html", {"data":datas})
    return HttpResponse("Nope.")

def new(request):
    return render(request, 'index/new.html')

def create(request):
    pass