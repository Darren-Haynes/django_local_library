from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Filter books containing the word "The"
    books_with_the = Book.objects.filter(title__contains="The")
    # books_with_the = ", ".join([book.title for book in books_filtered])

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres": num_genres,
        "books_with_the": books_with_the,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = (
        "book_list"  # your own name for the list as a template variable
    )
    queryset = Book.objects.all()

    template_name = "book_list.html"  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book

    template_name = "book_detail.html"  # Specify your own template name/location
