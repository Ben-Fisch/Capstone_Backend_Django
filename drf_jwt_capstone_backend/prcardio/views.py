from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from .models import PRCardio
from .serializers import PRCardioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class PRCardioList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        pr_cardio = PRCardio.objects.all()
        serializer = PRCardioSerializer(pr_cardio, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PRCardioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PRCardioDetail(APIView):

    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        try:
            return PRCardio.objects.get(pk=pk)
        except PRCardio.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pr_cardio = self.get_object(pk)
        serializer = PRCardioSerializer(pr_cardio)
        return Response(serializer.data)

    def put(self, request, pk):
        pr_cardio = self.get_object(pk)
        serializer = PRCardioSerializer(pr_cardio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pr_cardio = self.get_object(pk)
        pr_cardio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)