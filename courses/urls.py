from django.urls import path

from .views.coursres import *
from .views.session import *
from .views.rating import *


urlpatterns = [
    # Signup URL
    path('',coursres, name='coursres'),
    path('join_course/<int:course_id>/',join_course, name='join_course'),
    path('<int:course_id>/',course_details, name='course_details'),
    path('session/<int:session_id>/',session_details, name='session_details'),
    path("session/add/<int:course_id>",add_session, name="add_session"),
    path("session/delete/<int:session_id>",delete_session,name="delete_session"),
    path('student_attendance/<int:session_id>/',student_attendance, name='student_attendance'),
    path('generate_qrcode/<int:session_id>/',generate_qr_code, name='generate_qr_code'),
    
    path('session/<int:session_id>/rating/add/', add_session_rating, name='add_session_rating'),
    path('rating/<int:rating_id>/update/', update_session_rating, name='update_session_rating'),
    path('ratings/<int:session_id>/', session_rating_list, name='session_rating_list'),
]