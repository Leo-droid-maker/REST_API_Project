from django_filters import rest_framework as filters
from todoapp.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(filters.FilterSet):
    created = filters.NumberFilter(field_name='created', lookup_expr='contains')
    updated = filters.NumberFilter(field_name='updated', lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = ['project', 'created', 'updated']
