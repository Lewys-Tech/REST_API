from django.shortcuts import render
from django.http import JsonResponse
from book_api.models import Book

# Create your views here.
def book_list(request):
    books = Book.object.all() #complex data
    books_Python = list (books.values()) #python DS
    return JsonResponse({
        'books': books_Python
    })
    

