from . models import *
from . views import *

def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = cartlist.objects.filter(cart_id=c_id(request))
            cti = items.objects.all().filter(cart= ct[:1])
            for j in cti:
                item_count+=j.quant
        except cartlist.DoesNotExist:
            item_count = 0
        return dict(item_c=item_count)