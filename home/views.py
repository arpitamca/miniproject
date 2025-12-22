from django.shortcuts import render

# Create your views here.
def home_view(request):
    print("SESSION IN HOME VIEW:", dict(request.session))

    user_name = request.session.get('user_name')  # ✅ read from session
    print("HOME VIEW HIT ",user_name)
    return render(request, 'home.html', {
        'name': user_name
    })