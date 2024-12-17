from django.db import models

# Create your models here.
class Employee(models.Model):
    em_id = models.IntegerField(primary_key=True)
    em_name = models.CharField(max_length=125, blank=True)
    em_age = models.IntegerField(blank=True)

class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    dep_name = models.CharField(max_length=125, blank=True)
