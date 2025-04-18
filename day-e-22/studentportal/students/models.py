from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    class_name = models.CharField(max_length=20)
    marks = models.FloatField(max_length=30)

    def __str__(self):
        return self.name
    

