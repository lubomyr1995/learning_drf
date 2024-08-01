from django.db import models


class CarQuerySet(models.QuerySet):
    def less_then_year(self, year):
        return self.filter(year__lt=year)

    def only_sedan(self):
        return self.filter(body_type='Sedan')


class CarManager(models.Manager):
    def get_queryset(self):
        return CarQuerySet(self.model)

    def less_then_year(self, year):
        return self.get_queryset().less_then_year(year)

    def only_sedan(self):
        return self.get_queryset().only_sedan()
