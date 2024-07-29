from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer, CarSerializerWithAP


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


# class AutoParkAddCarView(GenericAPIView):
#     queryset = AutoParkModel.objects.all()
#
#     def post(self, *args, **kwargs):
#         auto_park = self.get_object()
#         data = self.request.data
#         serializer = CarSerializerWithAP(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(auto_park=auto_park)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class AutoParkCarListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = self.serializer_class(auto_park.cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
