from django.shortcuts import render,get_object_or_404,redirect
from ..models import Course,StudentsCourse,Session
from django.contrib.auth.decorators import login_required
from accounts.models import Student
@login_required(login_url='login')  
def coursres(request):
    coursres=Course.objects.all()
    return render(request,'courses/active.html',{'coursres':coursres})

@login_required(login_url='login')  
def join_course(request,course_id):
     course=get_object_or_404(Course,id=course_id)
     
     student=Student.objects.get(id=request.user.id)
     student_courses=StudentsCourse.objects.filter(student=student,course=course)
     if student_courses:
        return redirect('course_details',course.id)
     else:
         student_course=StudentsCourse.objects.create(student=student,course=course)
         return redirect('course_details',course.id)
     
@login_required(login_url='login')  
def course_details(request,course_id):
     course=get_object_or_404(Course,id=course_id)
     sessions=Session.objects.filter(course=course)
     print(sessions)
     return render(request,'courses/details.html',{'course':course})