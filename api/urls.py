from django.urls import path
from .views import students_list, student_detail

urlpatterns = [
    path('students/', students_list),
    path('students/<int:pk>/', student_detail),
]