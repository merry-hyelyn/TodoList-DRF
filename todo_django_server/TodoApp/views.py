from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    res = requests.get("127.0.0.1:8000/todo/posts/")

    print(res)
    pass