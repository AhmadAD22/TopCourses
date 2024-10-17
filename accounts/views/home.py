from django.shortcuts import render, redirect
from courses.models import StudentsCourse, Course
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  # Specify the URL name for your login view
def home(request):
    user = request.user
    courses = None
    if user.is_authenticated:
        courses = Course.objects.filter(studentscourse__student=user)    
    return render(request, 'home.html', {'courses': courses})
