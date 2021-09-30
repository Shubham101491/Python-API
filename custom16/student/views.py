from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# We using these as globally means for all APIs
from rest_framework.authentication import SessionAuthentication
from .custompermit import MyPermission

# Single class authenticate Permission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]