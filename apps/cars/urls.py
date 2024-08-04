from django.urls import path

from apps.cars.views import CarAddPhotoView, CarListView, CarRetrieveUpdateDestroyView, SedanListView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('/sedan', SedanListView.as_view(), name='sedan_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='car_retrieve_update_destroy'),
    path('/<int:pk>/photo', CarAddPhotoView.as_view(), name='car_add_photo'),
]
