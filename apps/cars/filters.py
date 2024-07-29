from django_filters import rest_framework as filters

from apps.cars.choices.body_type_choices import BodyTypeChoices


class CarFilter(filters.FilterSet):
    year_gte = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_lte = filters.NumberFilter(field_name='year', lookup_expr='lte')
    year_range = filters.RangeFilter('year')
    yeae_in = filters.NumberFilter('year')
    body = filters.ChoiceFilter('body_type', choices=BodyTypeChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            'brand',
            'price',
            # ('id', 'asd')
        )
    )
