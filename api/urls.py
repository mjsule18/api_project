from django.urls import path
from .views import StudentListAPIView, StudentDetailAPIView

urlpatterns = [
    path('students/', StudentListAPIView.as_view()),
    path('students/<int:pk>/', StudentDetailAPIView.as_view()),
]