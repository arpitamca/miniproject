from django.shortcuts import redirect, render

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
    veg_items = MenuItem.objects.filter(category='veg', available=True)

    veg_items = MenuItem.objects.filter(
        category='veg',
        available=True
    )

    nonveg_items = MenuItem.objects.filter(
        category='non veg',
        available=True
    )

    beverage_items = MenuItem.objects.filter(
        category='beverages',
        available=True
    )

    return render(request, 'menu.html', {
        'veg_items': veg_items,
        'nonveg_items': nonveg_items,
        'beverage_items': beverage_items,
    })

def admin_menu(request):
    if request.session.get("role") != "admin":
        return redirect("login")

    items = MenuItem.objects.all().order_by("category", "Item_name")

    return render(request, "admin/menu_list.html", {
        "items": items
    })

def add_menu_item(request):
    if request.session.get("role") != "admin":
        return redirect("login")

    if request.method == "POST":
        MenuItem.objects.create(
            Item_name=request.POST["name"],
            price=request.POST["price"],
            category=request.POST["category"],
            available=True
        )
        return redirect("admin_menu")

    return render(request, "admin/menu_form.html")


def edit_menu_item(request, item_id):
    if request.session.get("role") != "admin":
        return redirect("login")

    item = MenuItem.objects.get(id=item_id)

    if request.method == "POST":
        item.Item_name = request.POST["name"]
        item.price = request.POST["price"]
        item.category = request.POST["category"]
        item.available = "available" in request.POST
        item.save()

        return redirect("admin_menu")

    return render(request, "admin/menu_form.html", {
        "item": item
    })

def toggle_menu_item(request, item_id):
    if request.session.get("role") != "admin":
        return redirect("login")

    item = MenuItem.objects.get(id=item_id)
    item.available = not item.available
    item.save()

    return redirect("admin_menu")