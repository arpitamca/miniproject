import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteenQueue.settings')
django.setup()

from django.test import Client
from accounts.models import User

c = Client()
resp = c.post('/register/', {
    'name': 'Test User',
    'phone': '9999999999',
    'password': 'pass123',
    'role': 'student'
}, follow=True)

print('STATUS:', resp.status_code)
print('REDIRECT CHAIN:', resp.redirect_chain)
print('CONTENT SNIPPET:', resp.content.decode(errors='ignore')[:800])

# verify DB
u_count = User.objects.filter(phone='9999999999').count()
print('USERS_WITH_PHONE_9999999999:', u_count)
