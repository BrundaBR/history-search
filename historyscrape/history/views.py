from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .scrape import scrape_fun,detailInfo
import requests


def index(request):
    try:
        return_val=[]
        name=request.GET["box"]
        return_dictinory=scrape_fun(name)
        for key,value in return_dictinory.items():
            delt=detailInfo(value)
            string=" ".join(delt)
            return_val.append(string)
            break
        final_out=" ".join(return_val)
    except MultiValueDictKeyError:
        print("couldn't search!")
    return render(request,'index.html',{'txt':final_out})