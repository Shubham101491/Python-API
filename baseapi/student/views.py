from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Vard1
from .serializers import Vard1Serializer
from rest_framework.renderers import JSONRenderer

# Single Data
def vard1_detail(request, pk):
    # complex data
    vard = Vard1.objects.get(id=pk)
    # print(vard)
    # Convert into Python Data
    serializer = Vard1Serializer(vard)
    # print(serializer)
    # print(serializer.data)
    # Convert into Json Data
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data)  
    '''safe= False not required in dict, means id '''


# Query Set = All Student Data
def vard1_list(request):
    # complex data
    vard = Vard1.objects.all()
    # print(vard)
    # Convert into Python Data
    serializer = Vard1Serializer(vard, many=True)
    # print(serializer)
    # print(serializer.data)
    # Convert into Json Data
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

