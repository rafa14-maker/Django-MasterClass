from django_filters import rest_framework as filters

from .models import Product


class ProductsFilter(filters.FilterSet):
    keyword = filters.CharFilter(field_name="name", lookup_expr="icontains")
    min_price = filters.NumberFilter(field_name="price" or 0, lookup_expr="get")
    max_price = filters.NumberFilter(field_name="price" or 10000, lookup_expr="lte")

    class Meta:
        model = Product
        fields = ("keyword", "category", "brand")
