from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name    