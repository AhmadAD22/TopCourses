from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from ..models import Course,Attendance,Session,SessionRating
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
     return render(request,'sessions/details.html',{'session':session,'attendances': attendances,'session_rating':session_rating,'student_attendances':student_attendances})
    
@login_required(login_url='login')  
def student_attendance(request,session_id):
     session=get_object_or_404(Session,id=session_id)
     student=request.user
     attendance=Attendance.objects.filter(session=session,student=student,attended=True)
     if attendance:
         return redirect('session_details',session_id)
     else: 
        attendance=Attendance.objects.create(session=session,student=student,attended=True)
        return redirect('session_details',session_id)