from distutils.command.upload import upload
from lib2to3.pytree import Base
from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('Description', max_length=50, blank= False, null= False, unique= True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):
    description = models.CharField('Description', max_length=50, unique=True, null=False, blank= False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name= 'Descount indicator')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicator'

    def __str__(self):
        return f'Category offer: {self.descount_value} %'

class Product(BaseModel):
    name = models.CharField('Product name', max_length= 150, unique= True, blank= False, null= False)
    description = models.TextField('Product description', blank= True, null= True)
    image = models.ImageField('Product image', upload_to='products/', blank = True, null = True)

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Category offer: {self.description} %'
