from django.urls import path
from . import views


urlpatterns = [
    path('vardinfo/', views.vard1_list),
    path('vardinfo/<int:pk>', views.vard1_detail),
    
]
