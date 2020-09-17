from django.db import models

# Create your models here.

class Stock(models.Model):
    quantity = models.IntegerField(default=0)

class Items(models.Model):
    name = models.CharField('Наименование',max_length=100)
    cost = models.DecimalField('Стоимость',max_digits=6, decimal_places=2)
    # stock = models.OneToOneField(Stock, on_delete=models.CASCADE)

