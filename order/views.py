from django.contrib import messages
from urllib import request
from django.shortcuts import redirect, render

from accounts.models import User

# Create your views here.
from .models import MenuItem, Order, OrderItem
AVERAGE_PREP_TIME = 5

def add_to_order(request, menu_id):
    if request.method != "POST":
        return redirect("menu")
    # ✅ ALWAYS return response
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    try:
        user = User.objects.get(id=user_id)
        menu_item = MenuItem.objects.get(id=menu_id)
    except (User.DoesNotExist, MenuItem.DoesNotExist):
        return redirect("menu")

    order, _ = Order.objects.get_or_create(
        user=user,
        status="pending"
    )

    # 🎫 Assign token if missing
    if order.token_number is None:
        last_token = (
            Order.objects
            .filter(token_number__isnull=False)
            .order_by("-token_number")
            .first()
        )
        order.token_number = (last_token.token_number + 1) if last_token else 1
        order.save()

    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        menu_item=menu_item
    )

    if not created:
        order_item.quantity += 1
        order_item.save()

    messages.success(request, "🎉 Order placed successfully!")

    return redirect("menu")   # ✅ ALWAYS returns

    
    
def my_orders_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    user = User.objects.get(id=user_id)

    orders = Order.objects.filter(user=user).order_by("created_at")

    current_order = (
        Order.objects
        .filter(status="pending", token_number__isnull=False)
        .order_by("token_number")
        .first()
    )

    pending_orders = list(
        Order.objects
        .filter(status="pending")
        .order_by("created_at")
    )

    for order in orders:
        if order.status == "pending":
            position = pending_orders.index(order)
            order.eta_minutes = (position + 1) * AVERAGE_PREP_TIME
        else:
            order.eta_minutes = 0

    return render(request, "my_orders.html", {
        "orders": orders,
        "current_token": current_order.token_number if current_order else None
    })

def cancel_order(request, order_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    try:
        order = Order.objects.get(
            id=order_id,
            user_id=user_id,
            status="pending"
        )
    except Order.DoesNotExist:
        messages.error(request, "❌ Order cannot be cancelled")
        return redirect("my_orders")

    order.status = "cancelled"
    order.token_number = None
    order.save()

    messages.success(request, "❌ Order cancelled successfully")

    return redirect("my_orders")


def admin_dashboard(request):
    # 🔐 Admin protection
    if request.session.get("role") != "admin":
        return redirect("login")

    # All pending orders in token order
    pending_orders = (
        Order.objects
        .filter(status="pending")
        .order_by("token_number")
    )

    running_order = pending_orders.first()
    next_order = pending_orders[1] if pending_orders.count() > 1 else None

    return render(request, "admin/dashboard.html", {
        "running_token": running_order.token_number if running_order else None,
        "next_token": next_order.token_number if next_order else None,
        "pending_count": pending_orders.count(),
        "orders": pending_orders
    })

def serve_order(request, order_id):
    if request.session.get("role") != "admin":
        return redirect("login")

    try:
        order = Order.objects.get(id=order_id, status="pending")
    except Order.DoesNotExist:
        return redirect("admin_dashboard")

    order.status = "completed"
    order.save()

    return redirect("admin_dashboard")