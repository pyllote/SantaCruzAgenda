from rest_framework import serializers, pagination
from .models import Person, Reunion, Hobby


class HobbySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hobby
        fields = ('__all__')


 
class PersonSerializer(serializers.ModelSerializer):

    hobbies = HobbySerializer(many=True) # Con esto me aseguro  de ver el detalle de los hobbies

    class Meta:
        model= Person
        fields = ('__all__')


#--Creamos un serializador que no depende de un modelo

class PersonaSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required=False)


"""
Podemos poner información extra a un serializador que depende de un modelo

activo = serializers.BooleanField(required=False) #-- Aqui le incorporamos un campo nuevo

class PersonSerializer2(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = ('id','full_name','job','email','phone')
"""


class ReunionSerializer(serializers.ModelSerializer):

    person = PersonSerializer()

    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'person',
           
        )



#--Creamos un nuevo serializador para incorporar un método dentro de el

class ReunionSerializer2(serializers.ModelSerializer):

    fecha_hora = serializers.SerializerMethodField() # Esto me permite incoporar el método
    person = PersonSerializer() # Este me permite tener el detalle de la persona y evitar ver solamente el id

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'person',
            'fecha_hora',
        )
    
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)


#--Creamos un serializer que contendrá un link

class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'person',
        )
        extra_kwargs = {
            'person': {'view_name': 'persona:detallepersona', 'lookup_field': 'pk'}
        }



class PersonPagination(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 100


class CountReunionSerializer(serializers.Serializer):
    person__job = serializers.CharField()
    cantidad = serializers.IntegerField()