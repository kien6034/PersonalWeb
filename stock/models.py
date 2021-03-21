from django.db import models

# Create your models here.
class Stock(models.Model):
    NODATA = 'ND'
    GOOD = 'GO'
    MEDIUM = 'ME'
    BAD = 'BA'

    STATE_CHOICES = [
        (NODATA, 'No data'),
        (GOOD, 'Good'),
        (MEDIUM, 'Medium'),
        (BAD, 'Bad')
    ]
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=5)
    state = models.CharField(max_length=2,choices = STATE_CHOICES, default= NODATA)
    buy = models.FloatField(default=0)
    sell = models.FloatField(default=0)
    is_owned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code}"


class Figure(models.Model):
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE, related_name="figure")
    year = models.IntegerField()
    revenue = models.IntegerField()
    revenueP = models.FloatField(default=0)
    eps = models.FloatField()
    epsP = models.FloatField(default=0)
    equity = models.IntegerField(default=0)
    equityP = models.FloatField(default=0)
    PE = models.FloatField(default=0)
    

class Overview(models.Model):
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)
    crPrice = models.FloatField(default=0)
    crEPS = models.FloatField(default=0)
    crPE = models.FloatField(default=0)

    def __str__(self):
        return f"{self.stock.code}"



class WatchList(models.Model):
    name = models.CharField(max_length=256)
    stocks = models.ManyToManyField(Stock, related_name="stocks")