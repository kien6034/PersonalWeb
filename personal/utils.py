from .models import *
import datetime

excellentT = 95
goodT = 90
mediumT = 75

def update_day_score(last_day):
    tasks = last_day.dayTask.all()
    total_weight = 0
    total_finished_weight = 0
   
    for task in tasks:
        total_weight += task.weight
        if task.finished:
            total_finished_weight += task.weight
    
    if total_weight != 0:
        score = round(total_finished_weight / total_weight, 2) * 100
        last_day.total_finished_weight = total_finished_weight
        last_day.total_weight = total_weight
        last_day.score = score
        last_day.save()
    

def update_week_weight(last_week):
    tasks = last_week.weekTask.all()

    total_weight = 0
    total_finished_weight = 0

    for task in tasks:
        total_weight += task.weight
        if task.finished:
            total_finished_weight += task.weight
    
    #TODO: consider days perform
    if total_weight != 0:
        score = round(total_finished_weight / total_weight, 2) * 100
        
        last_week.total_finished_weight = total_finished_weight
        last_week.total_weight = total_weight
        last_week.save()


def create_automate_tasks(day):
    auto_tasks = AutoCreatedTask.objects.all()

    for task in auto_tasks:
        DayTask.objects.create(day=day, name = task.name, weight=task.weight)

    

def week_reward(week):
    days = week.myday.all()
    portfolio = Portfolio.objects.first()

    total_day_score = 0
    week_score = 0
    score = 0
    #calculate total day score
    for day in days:
        total_day_score += day.score
    
    #nomalize to 100 scale
    avg_dayscore = total_day_score / 7

    #calculate reward
    if week.total_weight != 0:
        week_score = week.total_finished_weight/week.total_weight * 100
        
        #score = 0.5 * avg_dayscore + 0.5 * weekscore
        score = portfolio.day_score_weight * avg_dayscore + (1 - portfolio.day_score_weight) * week_score
    else: 
        score = portfolio.day_score_weight * avg_dayscore
    
    print(score) # 23

    #reward = (score - threshold) / (1 - threshold) * weekly_money
    reward = ((int(score) - portfolio.thresh_hold) / (100-portfolio.thresh_hold)) * portfolio.weekly_money 
    
    week.score = int(score)
    week.save()

    portfolio.available_money += int(reward)
    portfolio.save()


def day_reward(day):
    portfolio = Portfolio.objects.first()

   
    reward = portfolio.daily_money * ((day.score - portfolio.thresh_hold) / (100 - portfolio.thresh_hold))
    portfolio.available_money += int(reward)
    day.reward = int(reward)
    portfolio.save()
    day.save()


def get_day_in_week(week):
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    start_date = week.startDate
    x = datetime.datetime.now()

    currentDate = x.date()

    day_in_week = dict()

    temp = start_date

    existed_day = list(week.myday.all())

    today = existed_day.pop()
    print('hey')
    for day in existed_day:
        print(day)
        pass

    for i in range(7):
        new_date = temp + datetime.timedelta(days=1)
        temp = new_date
        if temp > currentDate:
            #day_in_week[(days[temp.weekday()]] =
            pass
      
        
        
     

 