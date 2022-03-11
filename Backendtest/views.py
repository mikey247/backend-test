
from django.shortcuts import render
from Backendtest.models import Profile
from Backendtest.serializers import ProfileSerializer
from rest_framework import generics

# Create your views here.

class ProfileList(generics.ListAPIView):
    model=Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer




class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDelete(generics.DestroyAPIView):
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdate(generics.UpdateAPIView):
      queryset = Profile.objects.all()
      serializer_class = ProfileSerializer
