from django_filters import rest_framework as filters
from todoapp.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    created = filters.DateFilter(field_name='created', lookup_expr='gte')
    updated = filters.DateFilter(field_name='updated', lookup_expr='lte')

    class Meta:
        model = ToDo
        fields = ['project', 'created', 'updated']
