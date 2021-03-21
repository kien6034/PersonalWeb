from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyDay)
admin.site.register(DayTask)
admin.site.register(WeekTask)
admin.site.register(MyWeek)
admin.site.register(Quote)
admin.site.register(Portfolio)
admin.site.register(TaskGroup)
admin.site.register(Task)
admin.site.register(AutoCreatedTask)


