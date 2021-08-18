from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage


# Create your views here.


def home(request, c_slug=None):
    c_page = None
    prdt = None
    catgry = categ.objects.all()

    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prdt = product.objects.filter(category=c_page, available=True)
    else:
        prdt = product.objects.all().filter(available=True)
    paginator = Paginator(prdt, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'prdt': prdt, 'catgry': catgry,'pro':pro})


def prdct_details(request, c_slug, prdct_slug):
    try:
        prdt= product.objects.get(category__slug=c_slug,slug=prdct_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'prd':prdt})

# search option setting

def search(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)| Q(desc__contains=query))

    return render(request,'search.html', {'qr':query, 'prdt':prod})

