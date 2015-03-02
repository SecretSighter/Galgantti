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
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # percent_complete = models.DecimalField()

class Task_history(models.Model):
    task_id = models.ForeignKey('Task')
    user_id = models.ForeignKey('Collaborator')
    text = models.TextField(max_length=100)

class Attachment(BaseModel):
    task_id = models.ForeignKey('Task')
    user_id = models.ForeignKey('Collaborator')
    text = models.TextField(max_length=300)
    attachment_url = models.TextField(max_length=50)

class Comment(BaseModel):
    task_id = models.ForeignKey('Task')
    user_id = models.ForeignKey('Collaborator')
    text = models.TextField(max_length=300)

class Project(BaseModel):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    users = models.ManyToManyField('Collaborator')

class Configuration(BaseModel):
    project_id = models.ForeignKey('Project')
    key = models.TextField(max_length=50)
    value = models.TextField(max_length=50)