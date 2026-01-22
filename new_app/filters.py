import django_filters
from django import forms
from new_app.models import Product

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_by_all',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search products...',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Product
        fields = []

    def filter_by_all(self, queryset, name, value):
        return queryset.filter(
            productname__icontains=value
        ) | queryset.filter(
            category__icontains=value
        )
