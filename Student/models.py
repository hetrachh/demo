from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField('FirstName',max_length = 200)
    lname = models.CharField('LastName',max_length = 200)
    Enrollment = models.CharField('Enrollment',max_length = 200)
    email = models.CharField('Email',max_length = 200)
