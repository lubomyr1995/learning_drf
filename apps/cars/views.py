from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializerWithAP


# GenericAPIView
class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerWithAP
    filterset_class = CarFilter




class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerWithAP

