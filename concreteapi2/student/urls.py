from django.urls import path
from . import views

# pk  = primary key
urlpatterns = [
    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>', views.StudentRUD.as_view()),
    
]