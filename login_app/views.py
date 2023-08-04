from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def users(request):
    users = list(User.objects.all())
    context = {"total_users":len(users)}
    return render(request, 'users.html', context)

def creat_users(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        location = request.POST.get("location")
        career = request.POST.get("career")
        created = request.POST.get("created")

        new_user = User(created=created,
                        username=username,
                        career = career,
                        email=email,
                        password=password,
                        location = location)
        new_user.save()
    return redirect("users")
