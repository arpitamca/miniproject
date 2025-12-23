"""
URL configuration for canteenQueue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from accounts.views import login_view, logout_view,register_view
from home.views import home_view
from menu.views import add_menu_item, admin_menu, edit_menu_item, menu_view, toggle_menu_item, toggle_menu_item
from order.views import add_to_order, admin_dashboard, cancel_order, my_orders_view, serve_order

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'), 
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name="logout"),
    path('register/', register_view, name='register'),
    path('menu/', menu_view, name='menu'),
    path("add-to-order/<int:menu_id>/", add_to_order, name="add_to_order"),
    path("my-orders/", my_orders_view, name="my_orders"),
    path("cancel-order/<int:order_id>/", cancel_order, name="cancel_order"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("serve-order/<int:order_id>/", serve_order, name="serve_order"),
    path("canteen-admin/menu/", admin_menu, name="admin_menu"),
    path("canteen-admin/menu/add/", add_menu_item, name="add_menu_item"),
    path("canteen-admin/menu/edit/<int:item_id>/", edit_menu_item, name="edit_menu_item"),
    path("canteen-admin/menu/toggle/<int:item_id>/", toggle_menu_item, name="toggle_menu_item"),
]
