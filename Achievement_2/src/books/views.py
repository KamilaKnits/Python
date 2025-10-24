from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Book

# Create your views here.
# class-based view
class BookListView(ListView):
    # specify the model
    model = Book
    # specity the template
    template_name = 'books/main.html'

class BookDetailView(DetailView):
    # specify the model
    model = Book
    #specify the template
    template_name = 'books/detail.html'