from django.shortcuts import render, redirect
 #render shows HTML page, redirect sends user to another URL, 
 # User is imported to create new user
from .models import User

# Create your views here.
def login_view(request):
    error = None
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        try:
            user = User.objects.get(phone=phone, password=password)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name 
            return redirect('/home/')
        except User.DoesNotExist:
            error = "Invalid phone or password."

    return render(request, 'auth.html', {'error': error})

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        if password != confirm_password:
            error = "Passwords do not match"
            return render(request, 'auth.html', {'error': error})

        # (Optional but recommended) check duplicate email/phone
        if User.objects.filter(email=email).exists():
            error = "Email already exists"
            return render(request, 'auth.html', {'error': error})

        if User.objects.filter(phone=phone).exists():
            error = "Phone number already exists"
            return render(request, 'auth.html', {'error': error})

        User.objects.create(
            name=name,
            phone=phone,
            email=email,
            password=password,
            role=role
        )
        message = "Registration successful. Please log in."

        return redirect('login')

    return render(request, 'auth.html') 

