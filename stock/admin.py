from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Figure)
admin.site.register(Stock)
admin.site.register(Overview)
admin.site.register(WatchList)