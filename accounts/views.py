from urllib import request
from django.shortcuts import render, redirect
 #render shows HTML page, redirect sends user to another URL, 
 # User is imported to create new user
from .models import User

# Create your views here.
def login_view(request):
    error = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['role'] = user.role

            if user.role == "admin":
                return redirect("admin_dashboard")
            return redirect("home")

        except User.DoesNotExist:
            error = "Invalid email or password."

    return render(request, 'auth.html', {
        'error': error,
        'active_form': 'login'
    })


def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        # Basic validation: ensure required fields present
        form_context = {
            'active_form': 'register',
            'form_data': {
                'name': name or "",
                'email': email or "",
                'phone': phone or "",
                'role': role or "",
            }
        }

        if not password or not confirm_password or password != confirm_password:
            form_context['error'] = "Passwords do not match"
            return render(request, 'auth.html', form_context)

        if User.objects.filter(email=email).exists():
            form_context['error'] = "Email already exists"
            return render(request, 'auth.html', form_context)

        if User.objects.filter(phone=phone).exists():
            form_context['error'] = "Phone number already exists"
            return render(request, 'auth.html', form_context)

        User.objects.create(
            name=name,
            phone=phone,
            email=email,
            password=password,
            role=role
        )

        return redirect('login')

    # 👇 IMPORTANT: GET request
    return render(request, 'auth.html', {
        'active_form': 'login'
    })



def logout_view(request):
    request.session.flush()   # ✅ clears all session data
    return redirect("login")
