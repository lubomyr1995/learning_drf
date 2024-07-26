from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from cars.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    print(query)
    print(query.items())
    for k, v in query.items():
        match k:
            # Price
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            # Year
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)
            # Searching by brand_name
            case 'brand_start_with':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_end_with':
                qs = qs.filter(brand__iendswith=v)
            case 'brand_search':
                qs = qs.filter(brand__icontains=v)
            # Ordering
            case 'order_by':
                order_field = v
                if order_field.lstrip('-') not in ['brand', 'price', 'year']:
                    raise ValidationError(f"Cannot sort by field {order_field}")
                qs = qs.order_by(order_field)
            case _:
                raise ValidationError(f"Filter {k} not supported")
    return qs
