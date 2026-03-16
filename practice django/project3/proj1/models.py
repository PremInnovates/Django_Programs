from django.db import models


# Create your models here.
class Student(models.Model):
    Student_Name=models.CharField(max_length=20)
    Student_ID=models.IntegerField()
    Student_Percentage=models.FloatField()

    def __str__(self):
        return self.Student_Name
