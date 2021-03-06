from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from .models import Weight
from .serializers import WeightSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class WeightList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        weight = Weight.objects.all()
        serializer = WeightSerializer(weight, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WeightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeightDetail(APIView):

    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Weight.objects.get(pk=pk)
        except  Weight.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        weight = self.get_object(pk)
        serializer = WeightSerializer(weight)
        return Response(serializer.data)

    def put(self, request, pk):
        weight = self.get_object(pk)
        serializer = WeightSerializer(weight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        weight = self.get_object(pk)
        weight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)