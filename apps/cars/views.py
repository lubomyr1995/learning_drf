from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.cars.filters import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializerWithAP


# GenericAPIView
class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerWithAP
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
        # Доступ до аутеризованоого юзера є в класі
        # print(self.request.user.profile.name, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # return super().get_queryset()


class SedanListView(ListAPIView):
    serializer_class = CarSerializerWithAP
    # queryset = CarModel.objects.only_sedan().less_then_year(2018)
    queryset = CarModel.objects.only_sedan()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializerWithAP

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)
