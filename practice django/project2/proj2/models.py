from django.db import models
class project2(models.Model):
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    marks=models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
