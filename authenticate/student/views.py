from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# We using these as globally means for all APIs
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Single class authenticate Permission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated,AllowAny]
    permission_classes = [IsAdminUser]