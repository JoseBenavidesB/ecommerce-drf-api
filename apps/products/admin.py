from django.contrib import admin
from .models import MeasureUnit, CategoryProduct, Indicator, Product 

# Register your models here.
admin.site.register(MeasureUnit)
admin.site.register(CategoryProduct)
admin.site.register(Indicator)
admin.site.register(Product)