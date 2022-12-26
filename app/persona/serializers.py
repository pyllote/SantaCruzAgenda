from rest_framework import serializers
from .models import Person
 
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields = ('id','full_name','job','email','phone')


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