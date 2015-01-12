from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=100)
    student_number = models.AutoField()
    average_mark = models.CharField(max_length=1)

class Enrollment(models.Model):
    marks_received = models.CharField()

class Seminary(models.Model):
    name = models.CharField(max_length=50)
    seminar_name = models.CharField(max_length=50)
    fees = models.

class Professor(models.Model):
    name
    address
    phone_number
    email_address
    salary