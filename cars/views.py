from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.forms import model_to_dict
from cars.models import CarModel


class CarListCreateView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        cars_model = CarModel.objects.all()
        cars = [model_to_dict(i) for i in cars_model]
        return Response(cars, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        car_data = self.request.data
        car_model = CarModel.objects.create(**car_data)
        return Response(model_to_dict(car_model), status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    @staticmethod
    def get(*args, **kwargs):
        pk = kwargs['pk']
        try:
            car_model = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Car not found', status=status.HTTP_404_NOT_FOUND)
        car = model_to_dict(car_model)
        return Response(car, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        car_data: dict = self.request.data
        pk = kwargs['pk']
        try:
            car_model = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response('Car not found', status=status.HTTP_404_NOT_FOUND)
        for k, v in car_data.items():
            setattr(car_model, k, v)
        car_model.save()
        return Response(model_to_dict(car_model), status.HTTP_200_OK)

    @staticmethod
    def delete(*args, **kwargs):
        pk = kwargs['pk']
        try:
            car_model = CarModel.objects.get(pk=pk)
            car_model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CarModel.DoesNotExist:
            return Response('Car not found', status=status.HTTP_404_NOT_FOUND)
