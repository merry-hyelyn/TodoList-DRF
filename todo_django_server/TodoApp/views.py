from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse, HttpRequest
# Create your views here.


def index(request):
    if request.method == "POST":
        res = requests.get("http://127.0.0.1:8080/todo/posts/", params = request.POST)
    
    else:
        res = requests.get("http://127.0.0.1:8080/todo/posts/",params = request.GET)
    
    if res.status_code == 200:
        datas = json.loads(res.content)     # python에서 사용하기 위해 string -> python object
        return render(request, "index.html", {"data":datas})
    return HttpResponse("Nope.")

def new(request):
    print(request.POST)
    
    if request.method == 'POST':
        res = requests.post("http://127.0.0.1:8080/todo/posts/", data = request.POST)
    
    else:
        return render(request, 'new.html')
    
    print(res.status_code)
    if res.status_code == 201:
        data = res.content     # api로 보내기 위해 object -> python 
        return HttpResponse(data)
    return HttpResponse("fail")