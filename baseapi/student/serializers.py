from django.db import models
from rest_framework import fields, serializers
from .models import Vard1


class Vard1Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    contact = serializers.IntegerField()
    profession = serializers.CharField(max_length=50)
