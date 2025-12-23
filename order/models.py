from django.db import models

from accounts.models import User
from menu.models import MenuItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
    token_number = models.IntegerField(null=True, blank=True)  # 🎫 TOKEN

    def __str__(self):
        return f"Order {self.id} - {self.user.name}"

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)