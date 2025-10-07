from django.shortcuts import render
from django.http import HttpResponse
import random
from django.utils import timezone


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import random
from . import models 
from django.db.models import Avg

#Listview
def book_list_view(request):
    if request.method == 'GET':
        books = models.Books.objects.all()
        context = {
            'books': books, 
        }
        return render(request, template_name='books/book_list.html', context=context)
    
#Detailview
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        average_score = book_id.reviews.aggregate(Avg('mark'))['mark__avg']
        reviews = book_id.reviews.all()
        context = {
            'book_id': book_id,
            'average_score': average_score,
            'reviews': reviews,
        }
        return render(request, template_name='books/book_detail.html', context=context)

def current_time(request):
    now = timezone.localtime(timezone.now())
    return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"Случайное число: {number}")

def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут Ариана.Я увлекаюсь программированием,философией и психологией.")




def current_time(request):
    now = timezone.localtime(timezone.now())
    return HttpResponse(f"Текущее время: {now.strftime('%H:%M:%S')}")
 

def random_number(request):
    number = random.randint(1, 100)
    return HttpResponse(f"Случайное число: {number}")

def about_me(request):
    if request.method == 'GET':
        return HttpResponse("Меня зовут Ариана.Я увлекаюсь программированием,философией и психологией.")