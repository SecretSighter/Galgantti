#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'galgantti.settings'
import django
from django.db.models import Avg
django.setup()

# import models and run django/python commands
from base_app import models as hmod
# hmod.Enrollment.objects.all().delete()
# hmod.Seminar.objects.all().delete()
# hmod.Student.objects.all().delete()
# hmod.Professor.objects.all().delete()
hmod.MyUser.objects.all().delete()

MyUser1 = hmod.MyUser(first_name='user1', last_name='user1', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user2', last_name='user2', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user3', last_name='user3', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user4', last_name='user4', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user5', last_name='user5', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user6', last_name='user6', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user7', last_name='user7', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user8', last_name='user8', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user9', last_name='user9', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user10', last_name='user10', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user11', last_name='user11', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user12', last_name='user12', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user13', last_name='user13', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user14', last_name='user14', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user15', last_name='user15', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user16', last_name='user16', salary='20000')
MyUser1.save()

MyUser1 = hmod.MyUser(first_name='user17', last_name='user17', salary='20000')
MyUser1.save()


# professor = hmod.Professor(name='Conan Albrecht', email_address='conan@byu.edu', phone_number='8014224222')
# professor.address = 'Somewhere over the rainbow'
# professor.salary = 120000.00
# professor.save()

# professor2 = hmod.Professor(name='Gove Allen', email_address='gove@byu.edu', phone_number='8014224224')
# professor2.address = '7nth Floor'
# professor2.salary = 115000.00
# professor2.save()

# student = hmod.Student()
# student.name = 'Bruce Wayne'
# student.address = 'Gotham City'
# student.email_address = 'bruce@byu.net'
# student.phone_number = '8014224225'
# student.average_mark = 'A'
# student.save()

# student2 = hmod.Student()
# student2.name = 'Kal El'
# student2.address = 'Krypton'
# student2.email_address = 'superman@byu.net'
# student2.phone_number = '8014224226'
# student2.average_mark = 'B'
# student2.save()

# student3 = hmod.Student()
# student3.name = 'Jet Li'
# student3.address = 'China Provo Town'
# student3.email_address = 'jetli@byu.net'
# student3.phone_number = '8014224983'
# student3.average_mark = 'C'
# student3.save()

# seminar1 = hmod.Seminar(professor=professor, name='Math', seminar_number=1,fees='100.00')
# seminar1.save()

# seminar2 = hmod.Seminar(professor=professor2, name='Science', seminar_number=2, fees='150.00')
# seminar2.save()

# seminar2.student_on_waiting_list.add(student3)
# seminar2.save()

# seminar3 = hmod.Seminar(name='IS', seminar_number=3, fees=0.0)
# seminar3.save()

# enrollment1 = hmod.Enrollment(marks_received = 'A', student = student, seminar = seminar1)
# enrollment2 = hmod.Enrollment(marks_received = 'B', student = student2, seminar = seminar2)
# enrollment1.save()
# enrollment2.save()

# professors = hmod.Professor.objects.all()

# print('Professors Found in Database: \n')

# for professor in professors:
#     print('Professor ' + professor.name)

# students = hmod.Student.objects.all().order_by('email_address')

# print('\n\n\nStudents found in Database: \n')

# for student in students:
#     print(student.name + ' with email of ' + student.email_address)

# print('\n\nSeminar: \n')

# try:
#     oneSeminar = hmod.Seminar.objects.get(seminar_number=2)

#     print('Seminar of number ' + str(oneSeminar.seminar_number) + ' taught by ' + oneSeminar.professor.name + ' has a name of ' + oneSeminar.name + ' with fees of $' + str(oneSeminar.fees) + '.')

#     enrollments = oneSeminar.enrollment_set.all()
#     for enrollment in enrollments:
#         print (enrollment.student.name + ' received a mark of ' + enrollment.marks_received)

#         students_on_waiting_list = oneSeminar.student_on_waiting_list.all()
#     for student in students_on_waiting_list:
#         print('Student of name ' + student.name + ' is on the waiting list')

# except Exception:
#     print('Unable To Find Seminar')


# averageFee = hmod.Seminar.objects.filter(fees__gt=0).aggregate(Avg('fees'))
# print(averageFee['fees__avg'])
# seminarWithMaxFee = hmod.Seminar.objects.all().order_by('fees')[0]
# print('Max fee is ' + str(seminarWithMaxFee.fees))
# seminarWithMinFee = hmod.Seminar.objects.filter(fees__gt=0).order_by('-fees')[0]
# print('Min fee is ' + str(seminarWithMinFee.fees))

# seminarsWithoutTeachers = hmod.Seminar.objects.filter(professor__isnull=True)
# print('\n\nSeminars without teachers: \n')
# for seminar in seminarsWithoutTeachers:
#     print(seminar.name)

# studentsInProvo = hmod.Student.objects.filter(address__contains='Provo')
# print('\n\nStudents in Provo: \n')
# for student in studentsInProvo:
#     print(student.name)

# totalStudents = hmod.Student.objects.all().count()
# print('Total students: '+ str(totalStudents))

# totalProfessors = hmod.Professor.objects.all().count()
# print('Total Professors: ' + str(totalProfessors))

# totalSeminars = hmod.Seminar.objects.all().count()
# print('Total Seminars: ' + str(totalSeminars))