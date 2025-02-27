from django.shortcuts import render, redirect
from courses.models import StudentsCourse, Course
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  # Specify the URL name for your login view
def home(request):
    user = request.user
    courses = None
    
    if user.is_authenticated and hasattr(user, 'student'):
        # Assuming the logged-in user is a student and has a related Student profile
        student_courses = StudentsCourse.objects.filter(student=user.student)
        courses = [sc.course for sc in student_courses][:3]  # Get the first 3 courses
    
    return render(request, 'home.html', {'courses': courses})