from tabnanny import verbose
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    state           = models.BooleanField('Status', default=True)
    created_date    = models.DateField('Created date', auto_now=True, auto_now_add=False)
    modified_date   = models.DateField('Modified date', auto_now=True, auto_now_add=True)
    deleted_date    = models.DateField('Deleted date', auto_now=True, auto_now_add=False)


    class Meta:
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
