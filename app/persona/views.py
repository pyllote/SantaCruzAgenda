from django.shortcuts import render
from rest_framework import generics

from .models import Person, Reunion
from .serializers import PersonSerializer, PersonaSerializer, ReunionSerializer

# Create your views here.

class PersonListApiView(generics.ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()



class PersonaCreateApiView(generics.CreateAPIView):

    serializer_class = PersonSerializer


class PersonDetailView(generics.RetrieveAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.filter()



class PersonActualizarView(generics.RetrieveUpdateAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.filter()



class PersonDeleteView(generics.DestroyAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.filter()


#--Creamos una vista para usar el serializador
#--Que no depende del modelo

class PersonApiLista(generics.ListAPIView):

    serializer_class = PersonaSerializer
    
    def get_queryset(self):
        return Person.objects.all()



class ReunionListApiView(generics.ListAPIView):

    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()