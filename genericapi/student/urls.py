from django.urls import path
from . import views

# pk  = primary key
urlpatterns = [
    path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    path('studentapi/<int:pk>', views.StudentDestroy.as_view()),

]
