import django_filters
from . models import Usage


class UsageFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    date_range = django_filters.DateRangeFilter(field_name='date')
    date_between = django_filters.DateFromToRangeFilter(field_name='date', label='Date (Between)')
    type = django_filters.CharFilter(field_name='type', lookup_expr='exact')

    class Meta:
        model = Usage
        fields = ['date', 'type']
