#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()

# import models and run django/python commands
from homepage import models as hmod
professor = hmod.Professor(name='Conan Albrecht', email_address='conan@byu.edu', phone_number='8014224222')
professor.address = 'Somewhere over the rainbow'
professor.salary = 120000.00
professor.save()

professor2 = hmod.Professor(name='Gove Allen', email_address='gove@byu.edu', phone_number='8014224224')
professor2.address = '7nth Floor'
professor2.salary = 115000.00
professor2.save()

student = hmod.Student()
student.name = 'Bruce Wayne'
student.address = 'Gotham City'
student.email_address = 'bruce@byu.net'
student.phone_number = '8014224225'
student.average_mark = 'A'

student.save()

student2 = hmod.Student()
student2.name = 'Kal El'
student2.address = 'Krypton'
student2.email_address = 'superman@byu.net'
student2.phone_number = '8014224226'
student2.average_mark = 'B'

student2.save()

seminar1 = hmod.Seminar(professor=professor, name='Math', seminar_number=1,fees='100.00')
seminar1.save()

professors = hmod.Professor.objects.all()

print('Professors Found in Database: \n')

for professor in professors:
    print('Professor ' + professor.name)

students = hmod.Student.objects.all().order_by('email_address')

print('\n\n\nStudents found in Database: \n')

for student in students:
    print(student.name + ' with email of ' + student.email_address)