from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
import random
import datetime
from personal.models import *
from .models import *


# Create your views here.
def month_review(request):
    x = datetime.datetime.now()
    currentDate = x.date()

    month = Month.objects.last()
    year = Year.objects.last()

    #if new month
    if int(x.strftime("%m")) != month.value:
        #if new year
        if int(x.strftime("%Y")) != year.name:
            year = Year.objects.create(name = int(x.strftime("%Y")))

        year.cash += month.cash
        #create new month
        month = Month.objects.create(year= year, name = x.strftime("%b"), value = int(x.strftime("%m")))

    year.save()
    
    context= {
        'year': year,
        'month': month
    }

    return render(request, "finance/finance.html", context= context)


def add_transaction(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            
            tValue = data['value']
            action = data['action']
            
            if "-- " in tValue:
                values = tValue.split("-- ")
                try: 
                    amount = int(values[1])
                except:
                    return HttpResponse("ERROR")

                # create transaction
                month = Month.objects.last()
                x = datetime.datetime.now()
                currentDate = x.date()
                
                #get year
                year = Year.objects.last()

                if action == "plus":
                    transaction = Transaction.objects.create(month=month, date=currentDate,name = values[0], amount=amount, action ="Plus")
                    month.total_earn += amount
                    month.cash += amount
                    year.total_earn += amount
                    year.cash += amount
                else:
                    transaction = Transaction.objects.create(month=month, date=currentDate,name = values[0], amount=amount, action = "Minus")
                    month.total_spend += amount
                    month.cash -= amount
                    year.total_spend += amount
                    year.cash -= amount

                month.save()
                year.save()
            else:
                return HttpResponse("ERROR")
            
            return HttpResponse(transaction.id)
        else:
            return HttpResponse("ERROR")
    except:
        return HttpResponse("ERROR")
        
    
   


def delete_transaction(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        transactionId = data['transactionId']
        tType = data['type']

        #reduce coressponding value
        month = Month.objects.last()
        year = Year.objects.last()
        
        if tType == "transaction":
            transaction = get_object_or_404(Transaction, id = int(transactionId))

            amount = transaction.amount
            if transaction.action == "Plus":
                month.total_earn -= amount
                year.total_earn -= amount
                year.cash -= amount
                month.cash -= amount
            else:
                month.total_spend -= amount
                year.total_spend -= amount
                year.cash += amount
                month.cash += amount
        elif tType == "transfer":
            transaction = get_object_or_404(Transfer, id = int(transactionId))

            amount = transaction.amount

            if transaction.tfrom == "Cash":
                month.cash += amount
                year.cash += amount
            elif transaction.tfrom == "Stock":
                month.stock += amount
                year.stock += amount
            elif transaction.tfrom == "Crypto":
                month.crypto += amount
                year.crypto += amount
            else:
                return HttpResponse("NOT INSTANSIATED")
            
            if transaction.tto == "Cash":
                month.cash -= amount
                year.cash -= amount
            elif transaction.tto == "Stock":
                month.stock -= amount
                year.stock -= amount
            elif transaction.tto == "Crypto":
                month.crypto -= amount
                year.crypto -= amount
            else:
                return HttpResponse("NOT INSTANSIATED")

        month.save()
        year.save()
        transaction.delete()

        return HttpResponse("SUCCEED")
    
    return HttpResponse("Not authorized")


def update_stock(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        oValue = data['value']
        oType = data['type']

        value = oValue.replace(",", "")

        year = Year.objects.last()
        month = Month.objects.last()
        
        if oType == "STOCK":
            year.stock = int(value)
            month.stock = int(value) 
        elif oType == "CRYPTO":
            year.crypto = float(value)
            month.crypto = float(value) 
        year.save()
        month.save()

        return HttpResponse("SUCCEED")

def add_transfer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        fromValue = data['fromValue']
        toValue = data['toValue']
        nameValue = data['nameValue']
        amountValue = data['amountValue']
        
        #create new transaction
        month = Month.objects.last()
        year = Year.objects.last()
        x = datetime.datetime.now()
        currentDate = x.date()
        amount = int(amountValue)

        try:
            transaction = Transfer.objects.create(month=month, date = currentDate, name=nameValue, amount=amount, tfrom=fromValue, tto=toValue)

            if transaction.tfrom == "Cash":
                month.cash -= amount
                year.cash -= amount
            elif transaction.tfrom == "Stock":
                month.stock -= amount
                year.stock -= amount
            elif transaction.tfrom == "Crypto":
                month.crypto -= amount
                year.crypto -= amount
            
            
            if transaction.tto == "Cash":
                month.cash += amount
                year.cash += amount
            elif transaction.tto == "Stock":
                month.stock += amount
                year.stock += amount
            elif transaction.tto == "Crypto":
                month.crypto += amount
                year.crypto += amount
            
            month.save()
            year.save()
        except:
            return HttpResponse("INTERNAL ERROR")

        return HttpResponse(transaction.id)
    return HttpResponse("INTERNAL ERROR")