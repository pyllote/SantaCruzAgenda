from django.shortcuts import render
from rest_framework import generics

from .models import Person
from .serializers import PersonSerializer

# Create your views here.

class PersonListApiView(generics.ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
