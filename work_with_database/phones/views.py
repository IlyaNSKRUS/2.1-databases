from django.shortcuts import render, redirect

from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == None:
        phones_all = Phone.objects.all()
    else:
        if sort == 'name':
            phones_all = Phone.objects.order_by('name')
        else:
            if sort == 'min_price':
                phones_all = Phone.objects.order_by('price')
            else:
                phones_all = Phone.objects.order_by('-price')
    context = {
        'phones': phones_all,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {
        'phone': phone,
    }
    return render(request, template, context)
