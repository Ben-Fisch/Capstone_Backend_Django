from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from .models import Lift
from .serializers import LiftSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class LiftList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        lift = Lift.objects.all()
        serializer = LiftSerializer(lift, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LiftDetail(APIView):

    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        try:
            return Lift.objects.get(pk=pk)
        except Lift.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        lift = self.get_object(pk)
        serializer = LiftSerializer(lift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lift = self.get_object(pk)
        lift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)