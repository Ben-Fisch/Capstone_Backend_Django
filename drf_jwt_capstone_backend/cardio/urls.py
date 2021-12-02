from django.http import request
from django.urls import path
from django.http import request
from django.urls import path
from cardio import views

urlpatterns = [
    path('cardio/', views.CardioList.as_view()),
    path('cardio/<int:pk>/', views.CardioDetail.as_view())

]