from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book
from books.converters import DateConverter


def books_view(request):
    template = 'books/books.html'
    books_all = Book.objects.all()
    for book in books_all:
        book.pub_data = DateConverter.to_url(DateConverter, book.pub_date)
    context = {
        'books': books_all,
    }
    return render(request, template, context)

def pub_date_book(request, pub_date):
    b = []
    template = 'books/book.html'
    books_all = list(Book.objects.all())
    print(type(books_all), f'books_all = {books_all}')
    pub_date = DateConverter.to_python(DateConverter, pub_date).date()
    print(type(pub_date), pub_date)
    books = []
    for book in books_all:
        b.append(book.pub_date)
        if book.pub_date == pub_date:
            book.pub_date = DateConverter.to_url(DateConverter, book.pub_date)
            books.append(book)

    # page_number = str(pub_date)
    # paginator = Paginator(books_all, 1)
    # page = paginator.get_page(page_number)
    context = {
        'books': books,
        # 'page': page,

    }
    return render(request, template, context)

# def books_view_pag(request):
#     template = 'books/book.html'
#     books_all = Book.objects.all()
#     print(type(books_all), books_all)
#     paginator = Paginator(books_all, 2)
#     page_date = request.GET.get('pub_date')
#     page = paginator.get_page(page_date)
#     context = {
#         'books': books_all,
#         'page': page,
#     }
#     return render(request, template, context)

