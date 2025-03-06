from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Book

class BookView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
class CreatBookView(CreateView):
    model = Book
    template_name = 'cret.html'
    context_object_name = 'books'
    fields = ['nomi','muallifi','isbn','holati','oluvchi','olingan_sanasi','beriladigan_sanasi']
class BookDetail(DetailView):
    model = Book
    template_name = 'detal.html'
    context_object_name = 'books'
class UpdateBookView(UpdateView):
    model = Book
    template_name = 'update.html'
    context_object_name = 'books'
    fields = ['nomi','muallifi','isbn','holati','oluvchi','olingan_sanasi','beriladigan_sanasi']
class DeletBookView(DeleteView):
    model = Book
    template_name = 'delet.html'
    context_object_name = 'books'
    success_url = reverse_lazy('home')

from .models import Book

class SearchView(ListView):
    model = Book
    template_name = 'search.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(nomi__icontains=query)
        return Book.objects.all()
