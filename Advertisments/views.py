from django.shortcuts import render

# Create your views here.

# Rest API for Mobile Appication Development

from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response


class AdvertismentList(APIView):
    
    def get(self,request):
        advertisment=AdvertismentInfo.objects.all()
        serialzer=AdvertismentInfoSerializer(advertisment,many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = AdvertismentInfoSerializer(data=request.data)
        print("********** IS")
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class AdvertismentSingleList(APIView):

        def get(self,request,pk):
            print("************************************")
            advertisment=AdvertismentInfo.objects.filter(id=pk)
            serialzer=AdvertismentInfoSerializer(advertisment,many=True)
            return Response(serialzer.data)

        def post(self, request, format=None):
            print(request.data)
            serializer = AdvertismentInfoSerializer(data=request.data)
            print("********** IS")
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 