from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# StudentViewSet with Router
router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    # when session are used
    path('auth/', include('rest_framework.urls',namespace='rest_framwork'))
]