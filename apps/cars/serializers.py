from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')


class CarSerializerBegin(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    year = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data:dict) -> CarModel:
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data: dict) -> CarModel:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
            return instance
