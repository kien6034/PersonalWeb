from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
from .models import *
from .utils import *

# Create your views here.
def home(request, arg1, arg2):
    
    selection = ""
    watchlist = ""
    if arg1 == "watchlist":
        watchlist = get_object_or_404(WatchList, id = int(arg2))
        selection = "watchlist"


    watchlists = WatchList.objects.all()

    context = {
        "selection": selection,
        "watchlists": watchlists,
        "watchlist": watchlist
    }
    return render(request, "stock/home.html", context = context)

def stock_info(request, arg1):

    stock = get_object_or_404(Stock, code = arg1)

    context = {
        "stock": stock
    }
    return render(request, "stock/info.html", context=context)



def update_stock(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cId = data['id']
        cType = data['type']
        cValue = data['value']
      
        #update cell value
        figure = get_object_or_404(Figure, id=int(cId))
        if cType == 'revenue':
            figure.revenue = int(cValue)
            
        elif cType == "eps":
            figure.eps = float(cValue)
        elif cType == "PE":
            figure.PE = float(cValue)
        elif cType == "equity":
            figure.equity = float(cValue)
        figure.save()
    return HttpResponse('Succeed')
    


def wl_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        text = data['data']
        wlId = data['wlId']

        inputs = text.split(" -- ")

        if len(inputs[0]) == 3:
            wl = get_object_or_404(WatchList, id = wlId)
            try:
                stock = Stock.objects.get(code = inputs[0].upper())
            except:
                stock = Stock.objects.create(code = inputs[0].upper(), name = inputs[1] )
         
            wl.stocks.add(stock)
                
        else:
            return HttpResponse("Wrong syntax")

    return HttpResponse(wl.name)