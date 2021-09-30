from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
# Creating Router Object
router = DefaultRouter()

# StudentViewSet with Router
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('',include(router.urls)),
]