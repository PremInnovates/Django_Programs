from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
    def __str__(self):
        return self.name