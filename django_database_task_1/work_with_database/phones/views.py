from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == 'name':
        show_phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        show_phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        show_phones = Phone.objects.all().order_by('-price')
    else:
        show_phones = Phone.objects.all()

    context = {'phones': show_phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    show_phones = Phone.objects.get(slug = slug)
    context = {'phone': show_phones}
    return render(request, template, context)
