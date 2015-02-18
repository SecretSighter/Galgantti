from django.db import models

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Priority(BaseModel):
    name = models.TextField(max_length=40)
    order = models.IntegerField()

class Collaborator(models.Model):
    email_address = models.TextField(max_length=100)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    profile_picture = models.TextField(max_length=100)

class Task(models.Model):
    parent_task = models.ForeignKey('Task')
    # user_id = models.ForeignKey()
    name = models.TextField(max_length=100)
    priority = models.ForeignKey('Priority')


# class Professor(models.Model):
#     name = models.TextField(max_length=50)
#     address = models.TextField(max_length=100)
#     phone_number = models.TextField(max_length=15)
#     email_address = models.TextField(max_length=100)
#     salary = models.DecimalField(max_digits=9, decimal_places=2)
#
# class Seminar(models.Model):
#     name = models.TextField(max_length=50)
#     seminar_number = models.IntegerField()
#     fees = models.DecimalField(max_digits=6, decimal_places=2)
#     professor = models.ForeignKey('Professor', null=False)
#     student_on_waiting_list = models.ManyToManyField(Student)