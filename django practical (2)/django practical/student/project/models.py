from django.db import models

# Create your models here.
class student(models.Model):
    student_id =models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name