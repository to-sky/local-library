from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_author = Author.objects.count()
    num_genres = Genre.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instance': num_instance,
            'num_instances_available': num_instances_available,
            'num_author': num_author,
            'num_genres': num_genres
        }
    )