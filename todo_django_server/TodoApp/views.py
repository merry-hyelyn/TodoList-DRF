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
    if request.method == 'POST':
        res = requests.post("http://127.0.0.1:8080/todo/posts/", data = request.POST)
    else:   # GET이면 form 화면
        return render(request, 'new.html')
    
    if res.status_code == 201:
        data = res.content
        return redirect('../')
    return HttpResponse("fail")

def delete(request, id):
    pass

def detail(request, todo_id):
    res = requests.get("http://127.0.0.1:8080/todo/posts/",params = request.GET)
    datas = json.loads(res.content)
    for data in datas:
        if todo_id == data["id"]:
            detail_todo = {
                'title': data['title'],
                'content' : data['content'],
            }
    print(detail_todo)
    return render(request, "detail.html", {'detail' : detail_todo})

def update(request, todo_id):
    # res = requests.get("http://127.0.0.1:8080/todo/posts/",params = request.GET)
    # datas = res.content
    # for data in datas:
    #     if todo_id == data["id"]:
    #         detail_todo = {
    #             'title': data['title'],
    #             'content' : data['content'],
    #         }
    # return 
    pass
