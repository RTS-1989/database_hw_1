from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    phones = Phone.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'min_price':
        phones = phones.order_by('-price')
    elif sort_by == 'max_price':
        phones = phones.order_by('price')
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
