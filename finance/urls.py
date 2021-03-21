from django.urls import path
from finance import views

urlpatterns = [
    path("", views.month_review, name = "month_review"),
    path("month/add_transaction", views.add_transaction, name = "add_transaction"),
    path("month/delete_transaction", views.delete_transaction, name = "delete_transaction"),
    path("month/update_stock", views.update_stock, name = "update_stock"),
    path("month/add_transfer", views.add_transfer, name = "add_transfer"),
]