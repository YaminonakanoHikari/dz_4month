from django.contrib import admin
from .models import Customer, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'quantity', 'created_at')
