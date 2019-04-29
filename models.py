from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    major = models.TextField()
    grade = models.IntegerField()
    hometown = models.TextField()
