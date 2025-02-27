from django.urls import path
from .views.main import main
urlpatterns = [
    path('',main,name='trainer_main')
]
