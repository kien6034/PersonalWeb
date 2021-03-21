from django.db import models
from datetime import date
# Create your models here.

class Portfolio(models.Model):
    available_money = models.IntegerField(default=0)
    total_money = models.IntegerField(default=0)
    task_weight_money = models.IntegerField(default=0)
    weekly_money = models.IntegerField(default=0)
    daily_money = models.IntegerField(default=0)
    day_score_weight = models.FloatField(default=0)
    thresh_hold = models.IntegerField(default=0)

class Quote(models.Model):
    name = models.TextField()
    author = models.CharField(max_length = 256, default="Undefined")

    def __str__(self):
        return f"{self.name}"


class MyWeek(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    total_finished_weight = models.IntegerField(default=0)
    total_weight = models.IntegerField(default=0)
    score =models.FloatField(default=0)

    def __str__(self):
        return f"{self.startDate} to {self.endDate}"

class WeekTask(models.Model):
    week = models.ForeignKey(MyWeek, on_delete=models.CASCADE, related_name = "weekTask")
    name = models.CharField(max_length=256)
    finished = models.BooleanField(default=False)
    weight = models.IntegerField(default=0)

class MyDay(models.Model):
    week = models.ForeignKey(MyWeek, on_delete=models.CASCADE, related_name = "myday")
    date = models.DateField()
    score = models.IntegerField(default=0)
    total_weight = models.IntegerField(default= 0)
    total_finished_weight = models.IntegerField(default=0)
    noneed = models.CharField(max_length=256, null = True, blank=True)
    quote = models.ForeignKey(Quote, on_delete=models.SET_NULL, related_name="day_quote", null = True)
    reward = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.date}"

class DayTask(models.Model):
    day = models.ForeignKey(MyDay, on_delete=models.CASCADE, related_name="dayTask")
    name = models.CharField(max_length=256)
    finished = models.BooleanField(default=False)
    weight = models.IntegerField(default=0)


class TaskGroup(models.Model):
    name = models.CharField(max_length=256)
    sort_value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    group = models.ForeignKey(TaskGroup, on_delete = models.CASCADE, related_name="task")
    name = models.CharField(max_length=256)
    weight = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)


class AutoCreatedTask(models.Model):
    name = models.CharField(max_length=256)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"