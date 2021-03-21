from django.urls import path
from . import views

urlpatterns = [
    path("home/<arg1>/<arg2>", views.home, name="home"),
    path("info/<arg1>", views.stock_info, name = "stock"),
    path("stock/update", views.update_stock, name = "update_stock"),

    #api
    path("watchlist/add", views.wl_add, name = "wl_add"),
]