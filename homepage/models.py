from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=100)
    student_number = models.AutoField()
    average_mark = models.CharField(max_length=1)

class Seminar(models.Model):
    name = models.CharField(max_length=50)
    seminar_name = models.CharField(max_length=50)
    fees = models.DecimalField(max_digits=6, decimal_places=2)
    professor = models.ForeignKey('Professor')

class Enrollment(models.Model):
    marks_received = models.CharField()
    student = models.ForeignKey('Student')
    seminar = models.ForeignKey('Seminar')

class Professor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=9, decimal_places=2)