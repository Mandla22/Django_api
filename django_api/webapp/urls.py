from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.UsageList.as_view()),
]