from django.db import models

# 👇 define choices HERE (top of file)
CATEGORY_CHOICES = [
    ('veg', 'Veg'),
    ('non veg', 'Non-Veg'),
    ('beverages', 'Beverages'),
]

# Create your models here.
class MenuItem(models.Model):
    Item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100)

     # 👇 use choices HERE
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Item_name', 'category'],
                name='unique_menu_item'
            )
        ]


    def __str__(self):
        return f"{self.Item_name} ({self.get_category_display()})"
    