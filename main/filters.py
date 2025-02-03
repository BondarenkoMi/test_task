import django_filters
from .models import VPS, CHOICES


class VPSFilter(django_filters.FilterSet):
    cpu = django_filters.NumberFilter()
    ram = django_filters.NumberFilter()
    hdd = django_filters.NumberFilter()
    status = django_filters.ChoiceFilter(choices=CHOICES)

    class Meta:
        model = VPS
        fields = ('cpu', 'ram', 'hdd', 'status')