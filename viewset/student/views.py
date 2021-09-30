from re import S
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
# pk =primary key


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("***********LIst********")
        print("BAsename:", self.basename)
        print("Action:", self.action)
        print("detail:", self.detail)
        print("suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("***********Retrieve********")
        print("BAsename:", self.basename)
        print("Action:", self.action)
        print("detail:", self.detail)
        print("suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("***********Create********")
        print("BAsename:", self.basename)
        print("Action:", self.action)
        print("detail:", self.detail)
        print("suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, pk):
        print("***********Update********")
        print("BAsename:", self.basename)
        print("Action:", self.action)
        print("detail:", self.detail)
        print("suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print("***********Partial Update********")
        print("BAsename:", self.basename)
        print("Action:", self.action)
        print("detail:", self.detail)
        print("suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Partially Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print("***********Delete********")
        print("BAsename:", self.basename)
        print("Action:", self.action)
        print("detail:", self.detail)
        print("suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'Date Deleted'})
