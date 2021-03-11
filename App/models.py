from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Items(models.Model):

    name = models.CharField('Наименование', max_length=100, help_text="Наименование товара")
    cost = models.DecimalField('Стоимость', max_digits=6, decimal_places=2, help_text="Стоимость в долларах")
    text = models.CharField('Описание', max_length=255, help_text="Описание товара на 255 символов")
    link = models.CharField('Ссылка на картинку', max_length=255, help_text="URL адрес")

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.name


class Comments(models.Model):

    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField('Комментарий', max_length=255, help_text="Комментарий на 255 символов")
    date = models.DateField('Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return '{}: {} ({})'.format(self.user_id, self.text, self.date)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_customer')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DEVLIVERY = 'delivery'

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DEVLIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name='Заказчик', on_delete=models.CASCADE, related_name='related_orders')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказа',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)
    item = models.ForeignKey(Items, verbose_name='Комната', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)
