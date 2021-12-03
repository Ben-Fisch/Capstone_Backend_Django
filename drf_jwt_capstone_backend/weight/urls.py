from django.http import request
from django.urls import path
from weight import views

urlpatterns = [
    path('weight/', views.WeightList.as_view()),
    path('weight/<int:pk>/', views.WeightDetail.as_view())

]