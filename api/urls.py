from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDeleteView

urlpatterns = [
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteView.as_view()),
]