from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Course)
admin.site.register(StudentsCourse)
admin.site.register(Session)
admin.site.register(Attendance)
admin.site.register(SessionRating)
admin.site.register(QuestionTemplate)

