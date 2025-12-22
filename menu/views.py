from django.shortcuts import render

from menu.models import MenuItem

# Create your views here.
# def menu_view(request):
#     menu_items = MenuItem.objects.filter(available=True)
#     return render(request, 'menu.html', {
#         'menu_items': menu_items
#     })

# from django.shortcuts import redirect, get_object_or_404

from django.shortcuts import render
from menu.models import MenuItem

def menu_view(request):
    veg_items = (
        MenuItem.objects
        .filter(category='veg', available=True)
        .values('Item_name', 'price')
        .distinct()
    )

    nonveg_items = (
        MenuItem.objects
        .filter(category='non veg', available=True)
        .values('Item_name', 'price')
        .distinct()
    )

    beverage_items = (
        MenuItem.objects
        .filter(category='beverages', available=True)
        .values('Item_name', 'price')
        .distinct()
    )

    return render(request, 'menu.html', {
        'veg_items': veg_items,
        'nonveg_items': nonveg_items,
        'beverage_items': beverage_items,
    })
