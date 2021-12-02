from django.http import request
from django.urls import path
from lift import views

urlpatterns = [
    path('lifts/', views.LiftList.as_view()),
    path('lifts/<int:pk>/', views.LiftDetail.as_view())

]