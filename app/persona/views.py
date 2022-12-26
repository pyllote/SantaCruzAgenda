from django.shortcuts import render
from rest_framework import generics

from .models import Person, Reunion
from .serializers import PersonSerializer, PersonaSerializer, ReunionSerializer, \
    ReunionSerializer2, ReunionSerializerLink, PersonPagination, CountReunionSerializer

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

    #serializer_class = ReunionSerializer lo cambio para aplicar el serializer qeu trae el método
    serializer_class = ReunionSerializer2
    
    def get_queryset(self):
        return Reunion.objects.all()



class ReunionApiListaLink(generics.ListAPIView):
    
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()



class PersonPaginationLits(generics.ListAPIView):
    """
        lista personas con paginacion
    """

    serializer_class = PersonaSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()



class ReunionByPersonJob(generics.ListAPIView):

    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()