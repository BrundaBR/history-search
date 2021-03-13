from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .scrape import scrape_fun
import requests




def index(request):
    try:
        name=request.GET["box"]
        ret=scrape_fun(name)
        print(ret)

    except MultiValueDictKeyError:
        name=None

    return render(request,'index.html')