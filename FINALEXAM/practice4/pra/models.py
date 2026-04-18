from django.db import models

# Create your models here.
class Person(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    salary=models.FloatField()

def __str__(self):
    self.name
