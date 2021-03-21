from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Transaction)
#finance
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Transfer)