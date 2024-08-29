from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
#restframework views config
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Create your "api views" here.

class UserListCreateView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
