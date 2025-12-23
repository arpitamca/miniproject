from django.shortcuts import render, redirect
from accounts.models import User
from order.models import Order

AVERAGE_PREP_TIME = 5  # minutes

def home_view(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    user = User.objects.get(id=user_id)

    my_token = None
    expected_time = None
    expected_seconds = None
    running_token = None

    # 👤 User name
    user_name = user.name

    # 🎫 User's latest pending order
    user_order = (
        Order.objects
        .filter(user=user, status="pending")
        .order_by("created_at")
        .first()
    )

    # 🟢 Currently serving token
    current_order = (
        Order.objects
        .filter(status="pending", token_number__isnull=False)
        .order_by("token_number")
        .first()
    )

    # Defaults
    my_token = None
    expected_time = None
    running_token = current_order.token_number if current_order else None

    if user_order:
        my_token = user_order.token_number

        # Calculate ETA
        pending_orders = list(
            Order.objects
            .filter(status="pending")
            .order_by("created_at")
        )
        position = pending_orders.index(user_order)
        expected_time = (position + 1) * AVERAGE_PREP_TIME
        expected_seconds = expected_time * 60   # ✅ DO MATH HERE

    return render(request, "home.html", {
        "name": user_name,
        "my_token": my_token,
        "expected_time": expected_time,
        "running_token": running_token,
        "expected_seconds": expected_seconds,
    })
