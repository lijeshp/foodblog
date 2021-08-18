from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from cartapp.models import cartlist, items
from homeapp.models import product

# Create your views here.


def cartdetails(request,tot=0,count=0,ct_items=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart_id=ct, active=True)
        for i in ct_items:
            tot+=(i.prdct.price*i.quant)
            count+=i.quant
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'crt':ct_items,'tot':tot,'count':count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request,product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prdct=prod,cart=ct)
        if c_items.quant < c_items.prdct.stock:
            c_items.quant+=1
            c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prdct=prod,quant=1,cart=ct)
        c_items.save()
    return redirect('cartdetails')

def minus_cart(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prdt = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prdct=prdt,cart=ct)
    if c_items.quant > 1:
        c_items.quant-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')

def delete_cart(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prdt = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prdct=prdt,cart=ct)
    c_items.delete()
    return redirect('cartdetails')






