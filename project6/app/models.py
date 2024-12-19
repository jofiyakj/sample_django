from django.db import models

# Create your models here.
# class Employee(models.Model):
#     em_id = models.IntegerField(primary_key=True)
#     em_name = models.CharField(max_length=125, blank=True)
#     em_age = models.IntegerField(blank=True)

# class Department(models.Model):
#     dep_id = models.IntegerField(primary_key=True)
#     dep_name = models.CharField(max_length=125, blank=True)



# Create your models here.
class department(models.Model):
    dname=models.TextField()

    def __str__(self):
        return self.dname
class employee(models.Model):
    name=models.TextField()
    email=models.TextField()
    username=models.TextField()
    password=models.TextField()
    dname=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

