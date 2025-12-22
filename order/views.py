from django.shortcuts import redirect, render

from accounts.models import User

# Create your views here.
from .models import MenuItem, Order, OrderItem

def add_to_order(request):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("login")

        user = User.objects.get(id=user_id)
        menu_id = request.POST.get("menu_id")
        menu_item = MenuItem.objects.get(id=menu_id)

        # ✅ Get or create active order
        order, created = Order.objects.get_or_create(
            user=user,
            status="pending"
        )

        # ✅ If item already ordered → increase quantity
        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            menu_item=menu_item
        )

        if not created:
            order_item.quantity += 1
            order_item.save()

        return redirect("menu")
