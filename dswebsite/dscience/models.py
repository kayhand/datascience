from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=25)
    def __unicode__(self):
        return self.name

class Presentation(models.Model):
    topic = models.ForeignKey(Topic)
    first_due_date = models.DateTimeField('due date before meeting')
    upload_date = models.DateTimeField('presentation upload date')
    link = models.URLField(blank=True)
    pFile = models.FileField(upload_to='presentations', blank=True)
    def __unicode__(self):
        return self.topic.name

class Group(models.Model):
    name = models.CharField(max_length=25)
    presentation = models.ForeignKey(Presentation)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    group = models.ForeignKey(Group)
    def __unicode__(self):
        return self.user.username

class Assignment(models.Model):
    group = models.ForeignKey(Group)
    file = models.FileField(upload_to='assignments', blank=True)
    upload_due_date = models.DateTimeField('Assigned by admins')
    due_date = models.DateTimeField('due date of the assignment', blank=True, null=True)
    def __unicode__(self):
        return self.group.name

#Model to keep homeworks uploaded by users
class Homework(models.Model):
    assignment = models.ForeignKey(Assignment)
    user = models.ForeignKey(UserProfile) #Id of the user who uploads the hmw
    upload_date = models.DateTimeField('The date user made the upload')
    file = models.FileField(upload_to='homework')
    def __unicode__(self):
        return self.user.user.username

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')

field_score_options = [(1,1),(2,2),(3,3),(4,4),(5,5)]

#Calculate deadline on the fly
class Feedback(models.Model):
    user_giving_feedback = models.ForeignKey(UserProfile,related_name='feedback_giving')
    user_getting_feedback = models.ForeignKey(UserProfile,related_name='feedback_getting')
    presentation = models.ForeignKey(Presentation)
    due_date = models.DateTimeField()
    date_given = models.DateTimeField()
    clarity = models.IntegerField(choices=field_score_options)
    exposition = models.IntegerField(choices=field_score_options)
    smoothness = models.IntegerField(choices=field_score_options)
    qa = models.IntegerField(choices=field_score_options)
    comments = models.TextField()
    is_given = models.BooleanField()
    def __unicode__(self):
        return self.user_giving_feedback.user.username
    



    