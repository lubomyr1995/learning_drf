from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializerWithAP


# GenericAPIView
class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerWithAP
    filterset_class = CarFilter
    permission_classes = (AllowAny,)
    # def get_queryset(self):
    # Доступ до аутеризованоого юзера є в класі
    # print(self.request.user.profile.name, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    # return super().get_queryset()


class SedanListView(ListAPIView):
    serializer_class = CarSerializerWithAP
    # queryset = CarModel.objects.only_sedan().less_then_year(2018)
    queryset = CarModel.objects.only_sedan()
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerWithAP
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CarAddPhotoView(UpdateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarPhotoSerializer

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)
