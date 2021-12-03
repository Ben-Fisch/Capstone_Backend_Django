from django.http import request
from django.urls import path
from prlift import views

urlpatterns = [
    path('prlifts/', views.PRLiftList.as_view()),
    path('prlifts/<int:pk>/', views.PRLiftDetail.as_view())

]