from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Insert menu items using raw SQL"

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO menu_menuitem (Item_name, price, available, category) VALUES (%s, %s, %s, %s)",
                ["Sandwich", 80, True, 'veg']
            )
            #    cursor.execute("DELETE FROM menu_menuitem;")


        self.stdout.write(self.style.SUCCESS("Menu item inserted"))