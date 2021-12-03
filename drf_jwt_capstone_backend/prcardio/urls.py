from django.http import request
from django.urls import path
from prcardio import views

urlpatterns = [
    path('prcardio/', views.PRCardioList.as_view()),
    path('prcardio/<int:pk>/', views.PRCardioDetail.as_view())

]