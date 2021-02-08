from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stock(models.Model):
    quantity = models.IntegerField(default=0)

class Items(models.Model):
    name = models.CharField('Наименование',max_length=100,help_text="Наименование товара")
    cost = models.DecimalField('Стоимость',max_digits=6, decimal_places=2, help_text="Стоимость в долларах")
    text = models.CharField('Описание',max_length=255, help_text="Описание товара на 255 символов")
    # stock = models.OneToOneField(Stock, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

class Comments(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField('Комментарий', max_length=255, help_text="Комментарий на 255 символов")
    date = models.DateField('Дата', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.user_id, self.text)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'