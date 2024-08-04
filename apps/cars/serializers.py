from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ValidationError

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'photo', 'created_at', 'updated_at')

    # Validation in serializer
    def validate(self, data):
        if data['brand'] == 'XXX':
            raise ValidationError({'detail': 'this db not accept this brand'})
        return super().validate(data)

    def validate_year(self, year):
        if year == 1999:
            raise ValidationError({'details': 'year eq 1999'})
        return year


class CarSerializerWithAP(serializers.ModelSerializer):
    auto_park = StringRelatedField(read_only=True)

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type', 'photo', 'auto_park', 'created_at', 'updated_at')
        read_only_fields = ('auto_park', 'created_at', 'updated_at')


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}
