from rest_framework import generics

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer

""" -------------- Measure Unit------------------"""
class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

    
""" -------------- Indicator ------------------"""
class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

    
""" --------------  Category Product------------------"""
class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer

    