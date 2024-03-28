from django.contrib import admin
from django.urls import path
from book_api.views import BookCreate, BookList

urlpatterns = [
    path('',BookCreate.as_view()),
    path('list/', BookList.as_view()),
    #path('<int:pk>', book),
]
