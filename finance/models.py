from django.db import models

# Create your models here.
#finance

class Year(models.Model):
    name = models.IntegerField(default=0)
    total_earn = models.IntegerField(default=0)
    total_spend = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    crypto = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Month(models.Model):
    year = models.ForeignKey(Year, on_delete= models.CASCADE, related_name="month")
    name = models.CharField(max_length = 128, blank=True, null=True)
    value = models.IntegerField(default=0)
    score = models.FloatField(default=0)
    total_earn = models.IntegerField(default=0)
    total_spend = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    crypto = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="transaction")
    date = models.DateField()
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    ACTIONS = (
        ('Plus', 'Plus'),
        ('Minus', 'Minus')
    )
    action = models.CharField(max_length=5, choices = ACTIONS, blank= True, null = True)


class Transfer(models.Model):
    WALLET_TYPES = (
        ('Stock', 'Stock'),
        ('Spending', 'Spending'),
        ('Earning', 'Earning'),
        ('Cash', 'Cash'),
        ('Crypto', 'Crypto'),
        ('Avail', 'Avail')
    )
    
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name="transfer")
    date = models.DateField()
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    tfrom = models.CharField(max_length= 8, choices=WALLET_TYPES, blank=True, null=True)
    tto = models.CharField(max_length= 8, choices=WALLET_TYPES, blank=True, null=True)
   