from django.urls import path
from . import views

# pk  = primary key
urlpatterns = [
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),

]