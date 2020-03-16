from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import UsageSerializer
from . models import Usage
from .Filter import UsageFilter


class Filter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)

        if filter_class:
            return filter_class(request.query_params, queryset=queryset, request=request).qs
        return queryset


class UsageList(APIView):
    filter_class = UsageFilter
    serializer_class = UsageSerializer

    def get(self, request):
        queryset = Usage.objects.all()
        f = Filter()
        filtered_queryset = f.filter_queryset(request, queryset, self)
        serialized = UsageSerializer(queryset, many=True)
        if filtered_queryset.exists():
            serialized = UsageSerializer(filtered_queryset, many=True)

        return Response(serialized.data)

    def post(self, request):
        data_ = request.data
        data_object = UsageSerializer(data=data_)
        if data_object.is_valid(raise_exception=True):
            saved_obj = data_object.save()
            current_month = saved_obj.date.month
            current_year = saved_obj.date.year

            usage_list = Usage.objects.filter(date__month=current_month)\
                .filter(date__year=current_year)
            total_amount = 0
            for usage in usage_list:
                total_amount += usage.amount

            return_obj = {
                'posted-object': data_object.data,
                'total-amount': total_amount
            }

        return Response(return_obj)
