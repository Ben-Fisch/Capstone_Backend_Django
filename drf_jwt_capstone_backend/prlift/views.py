from django.http import request
from django.http.response import Http404
from django.shortcuts import render
from .models import PRLift
from .serializers import PRLiftSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class PRLiftList(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        pr_lift = PRLift.objects.all()
        serializer = PRLiftSerializer(pr_lift, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PRLiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PRLiftDetail(APIView):

    permission_classes = [AllowAny]
    
    def get_object(self, pk):
        try:
            return PRLift.objects.get(pk=pk)
        except PRLift.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pr_lift = self.get_object(pk)
        serializer = PRLiftSerializer(pr_lift)
        return Response(serializer.data)

    def put(self, request, pk):
        pr_lift = self.get_object(pk)
        serializer = PRLiftSerializer(pr_lift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pr_lift = self.get_object(pk)
        pr_lift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)