from django.db import models
from books.models import Books  # Импортируем модель Books

class Customer(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100, verbose_name="Имя покупателя")
    email = models.EmailField(null=True, blank=True,verbose_name="Email")
    phone = models.CharField(null=True, blank=True, max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,)

    def __str__(self):
        return f"Заказ {self.book.title} для {self.customer.name}"
