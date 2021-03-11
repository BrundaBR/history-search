from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.






def index(request):
    try:
        name=request.GET["box"]
        scrape(name)
    except MultiValueDictKeyError:
        name=None

    return render(request,'index.html')