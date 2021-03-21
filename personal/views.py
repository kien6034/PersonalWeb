from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
import random
import datetime
from .models import *
from .utils import *

def home(request):
    x = datetime.datetime.now()
    currentDate = x.date()
    
    myWeek = MyWeek.objects.last()

    #create new week when it comes to monday
    if currentDate == myWeek.endDate + datetime.timedelta(days = 1):
        week_reward(myWeek)
        myWeek = MyWeek.objects.create(startDate = currentDate, endDate = currentDate + datetime.timedelta(days=6))

    
    #update week weight
    update_week_weight(myWeek)

    #last day 
    lastDay = MyDay.objects.last()
    update_day_score(lastDay)
    
    if lastDay.date != currentDate:
        #create new day
        day_reward(lastDay)
        day = MyDay.objects.create(week = myWeek, date = currentDate)

        #automate created tasks
        create_automate_tasks(day) 
    else:
        day = lastDay
    
    #quote for day
    if not day.quote:
        #get random quote
        quotes = Quote.objects.all()

        quote = random.choice(quotes)
        
        day.quote = quote
        day.save()
    
    #remove the current day from previosu day list
    previousDays = list(myWeek.myday.all())
    currentDay = previousDays.pop()

    print(currentDate)
    context = {
        'weekDay': x.strftime("%A"),
        'currentDate': day,
        'week': myWeek,
        'dayTasks': day.dayTask.all(),
        'weekTasks': myWeek.weekTask.all(),  
        'previousDays': previousDays,
        'portfolio': Portfolio.objects.first(),
        'taskGroups': TaskGroup.objects.all()
    }

    return render(request, "personal/home.html", context = context)

def add_task(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        tValue = data['value']
        tType = data['type']
        
        if "-- " in tValue:
            inputs = tValue.split("-- ")
            ip = inputs[0]
            wg = int(inputs[1])
        else:
            ip = tValue
            wg = 0
        
     
        if tType == 'day':
            currentDay = MyDay.objects.last()
            newTask = DayTask.objects.create(day= currentDay, name = ip, weight =wg)
        elif tType == 'week':
            currentWeek = MyWeek.objects.last()
            newTask = WeekTask.objects.create(week=currentWeek, name = ip, weight =wg)

        data = {
            'name': ip,
            'weight': wg,
            'id': newTask.id,
        }
        return JsonResponse(data)   
    return HttpResponse('Not authorized')


def update_task(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        tId = data['id']
        tType = data['type']
        tChecked = data['isChecked']
        
        if tType == "day":
            #get the day task
            task = get_object_or_404(DayTask, id = int(tId))
            
            task.finished = tChecked
            task.save()
        elif tType == "week":
            task = get_object_or_404(WeekTask, id = int(tId))
            
            task.finished = tChecked
            task.save()
        return HttpResponse('SUCCEED')

    return HttpResponse('NOT AUTHORIZED')


def task(request, groupid):
    taskGroup = get_object_or_404(TaskGroup, id = groupid)
    portfolio = Portfolio.objects.first()

    context = {
        'group': taskGroup,
        'portfolio': portfolio,
    }
    return render(request, "personal/task.html", context=context)


def add_group_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mData = data['data']

        if "-- " in mData:
            inputs = mData.split("-- ")
            name = inputs[0]
            sortValue = int(inputs[1])
        else:
            name = mData
            sortValue = 0
        
        #create new group task
        try:
            groupTask = TaskGroup.objects.create(name = name, sort_value=sortValue)
        except:
            return HttpResponse("ERROR")
        return HttpResponse(groupTask.id)
    return HttpResponse("ERROR")

def group_add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        groupID = data['groupID']
        tValue = data['value']

        if "-- " in tValue:
            inputs = tValue.split("-- ")
            ip = inputs[0]
            wg = int(inputs[1])
        else:
            ip = tValue
            wg = 0

        group = get_object_or_404(TaskGroup, id = int(groupID))
        
        task = Task.objects.create(group= group, name=ip, weight=wg)

    return HttpResponse(ip)

def group_update_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tId = data['id']
        tChecked = data['isChecked']
        
        
        #get portfolio
        portfolio = Portfolio.objects.first()

        #get the day task
        task = get_object_or_404(Task, id = int(tId))
        
        if tChecked == True:
            portfolio.available_money += task.weight * portfolio.task_weight_money
            task.finished = tChecked
        elif tChecked == False:
            portfolio.available_money -= task.weight * portfolio.task_weight_money
            task.finished = tChecked   
        task.save()
        portfolio.save()
        return HttpResponse("SUCCEED")
    return HttpResponse('NOT AUTHORIZED')

def group_edit_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tType = data['type']
        tValue = data['value']
        tId = data['taskId']

        task = get_object_or_404(Task, id = int(tId))
        
        if tType == "name":
            task.name = tValue
            task.save()
        elif tType == "weight":
            try:
                weight = int(tValue)
            except:
                return HttpResponse("ERROR")
            
            if weight == 0:
                task.delete()
                return HttpResponse("DELETE")
            task.weight = weight
            task.save()

        return HttpResponse("SUCCEED")
    return HttpResponse("NOT AUTHORIZEDS")

def delete_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tType = data['type']
        tId = data['id']

        if tType == "day":
            task = get_object_or_404(DayTask, id = int(tId))
        elif tType == "week":
            task = get_object_or_404(WeekTask, id = int(tId))
        
        task.delete()

        return HttpResponse("SUCCEED")
    return HttpResponse("Not authorized")


def review_day(request, dId):
    return HttpResponse("TODO")