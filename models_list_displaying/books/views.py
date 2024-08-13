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

# def pub_date_book(request, pub_date):
#     b = []
#     template = 'books/book.html'
#     books_all = list(Book.objects.all())
#     print(type(books_all), f'books_all = {books_all}')
#     pub_date = DateConverter.to_python(DateConverter, pub_date).date()
#     print(type(pub_date), pub_date)
#     books = []
#     for book in books_all:
#         b.append(book.pub_date)
#         if book.pub_date == pub_date:
#             book.pub_date = DateConverter.to_url(DateConverter, book.pub_date)
#             books.append(book)
#
#     # page_number = str(pub_date)
#     # paginator = Paginator(books_all, 1)
#     # page = paginator.get_page(page_number)
#     context = {
#         'books': books,
#         # 'page': page,
#
#     }
#     return render(request, template, context)

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
def books_pub_date(request, pub_date):
    template = 'books/book.html'
    books_objects = Book.objects.filter(pub_date=pub_date)
    for x in books_objects:
        x.pub_date = DateConverter.to_url(DateConverter, x.pub_date)
    books_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    if books_next != None:
        books_next.pub_date = DateConverter.to_url(DateConverter, books_next.pub_date)
    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    if books_previous != None:
        books_previous.pub_date = DateConverter.to_url(DateConverter, books_previous.pub_date)
    context = {
        'books': books_objects,
        'next_book': books_next,
        'previous_book': books_previous,
    }
    return render(request, template, context)


# По аналогии с предыдущим ДЗ вы пытаетесь использовать встроенный Django-пагинатор.
# Но он под это задание не подходит. С его помощью можно создать навигацию по страницам, но не по датам.
# В этом задании нужно фильтровать книги по дате.
