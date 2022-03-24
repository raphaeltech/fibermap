from rest_framework import serializers
from inventory.models import positionPoles

class serializersPositionPoles(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    identification = serializers.CharField(max_length=256)
    geolocation = serializers.CharField(max_length=256)
    poleModel = serializers.CharField(max_length=256)
    isLocate = serializers.BooleanField(default=True)
    priceLocation = serializers.FloatField(max_length=256)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        :param validated_data:
        """
        return serializersPositionPoles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Person` instance, given the validated data.
        """

        instance.identification = validated_data.get(
            'Identificação', instance.identification)
        instance.geolocation = validated_data.get(
            'Geolocalização', instance.geolocation)
        instance.poleModel = validated_data.get('Modelo de Poste', instance.poleModel)
        instance.isLocate = validated_data.get(
            'Poste Locado', instance.isLocate)
        instance.priceLocation = validated_data.get('Modelo de Poste', instance.priceLocation)
        
        instance.save()
        return instance