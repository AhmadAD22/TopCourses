from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from ..models import Course,Attendance,Session,SessionRating,QuestionTemplate
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ..models import Session
from ..forms.session import SessionForm
from django.shortcuts import render
from django.db import IntegrityError
from accounts.models import Student



def sessions_by_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    sessions = Session.objects.filter(course=course)
    return render(request, 'sessions/sessions_by_course.html', {'course': course, 'sessions': sessions})

def toggle_active_status(request, pk):
    session = get_object_or_404(Session, pk=pk)
    session.active = not session.active
    session.save()
    return redirect('session_list')

@login_required(login_url='login')  
def generate_qr_code(request, session_id):
    # توليد رابط الحضور بناءً على session_id
    url = request.build_absolute_uri(reverse('student_attendance', args=[session_id]))

    # إنشاء QR code باستخدام مكتبة qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # إنشاء صورة QR code
    img = qr.make_image(fill='black', back_color='white')

    # تحويل الصورة إلى صيغة PNG
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    # إرجاع الصورة كـ HTTP response
    return HttpResponse(buffer, content_type='image/png')

@login_required(login_url='login')  
def session_details(request,session_id):
     session=get_object_or_404(Session,id=session_id)
     attendances = Attendance.objects.filter(session=session, attended=True)
     student_attendances=Attendance.objects.filter(session=session,student=request.user,attended=True)
     session_rating=SessionRating.objects.filter(session=session,student=request.user)  
     
     if session_rating:
         session_rating=session_rating.first()
     evaluation_tamplate=QuestionTemplate.objects.filter(session=session)
     return render(request,'sessions/details.html',
                   {'session':session,'attendances': attendances,
                    'session_rating':session_rating,
                    'student_attendances':student_attendances,
                    'evaluation_tamplate':evaluation_tamplate})
    
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  
def student_attendance(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if session.active:
        student = Student.objects.get(id= request.user.id)
        
        attendance = Attendance.objects.filter(session=session, student=student, attended=True).first()
        if attendance:
            return redirect('session_details', session_id=session_id)
        else: 
            Attendance.objects.create(session=session, student=student, attended=True)
            return redirect('session_details', session_id=session_id)
    else:
        raise Http404("Session is not active.")
    
def add_session(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.course = course
            try:
                session.save()
                return redirect('course_details', course_id=course_id)
            except IntegrityError:
                form.add_error('number','رقم الجلسة موجود بالفعل في هذا التدريب')
    else:
        form = SessionForm()
    return render(request, 'sessions/add.html', {'form': form, 'course': course})
         
            
def delete_session(request,session_id):
    session=get_object_or_404(Session,id=session_id)
    course_id=session.course.id
    session.delete()
    return redirect('course_details', course_id=course_id)
    