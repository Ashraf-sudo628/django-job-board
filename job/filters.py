import django_filters
from .models import JOb

class JobFilter(django_filters.FilterSet):
    Description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = JOb
        fields = '__all__'
        exclude = ['Published_At','image','Owner','Vacancy','slug']