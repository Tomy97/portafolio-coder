from django.db import models
from django.db.models.fields import CharField, IntegerField, DateField
class FamilyData(models.Model):
    edad =  IntegerField()
    nombre = CharField(max_length = 100)
    apellido = CharField(max_length = 100)
    BirthDay = DateField()

