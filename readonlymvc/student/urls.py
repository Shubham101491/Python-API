from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# StudentViewSet with Router
router.register('studentapi',views.StudentROM,basename='student')

urlpatterns = [
    path('',include(router.urls)),
]