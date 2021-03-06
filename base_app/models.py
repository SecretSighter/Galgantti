from django.db import models

class MyUser(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    salary = models.IntegerField()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

class Picture(BaseModel):
    filename = models.TextField(max_length=100)
    size = models.IntegerField()
    mime_type = models.TextField(max_length=100)
    title = models.TextField(max_length=100)

class File(BaseModel):
    filename = models.TextField(max_length=100)
    guid = models.IntegerField(max_length=100)
    location = models.TextField(max_length=100)

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