from django.db import models

class Student(models.Model):
    name = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=15)
    email_address = models.TextField(max_length=100)
    average_mark = models.TextField(max_length=1)

class Enrollment(models.Model):
    marks_received = models.TextField(max_length=50)
    student = models.ForeignKey('Student')
    seminar = models.ForeignKey('Seminar')

class Professor(models.Model):
    name = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=15)
    email_address = models.TextField(max_length=100)
    salary = models.DecimalField(max_digits=9, decimal_places=2)

class Seminar(models.Model):
    name = models.TextField(max_length=50)
    seminar_number = models.IntegerField()
    fees = models.DecimalField(max_digits=6, decimal_places=2)
    professor = models.ForeignKey('Professor')
    student_on_waiting_list = models.ManyToManyField(Student)