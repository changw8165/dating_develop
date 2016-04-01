from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseDetails(models.Model):
      title = models.CharField(max_length=25)
      duration = models.CharField(max_length=50)
      price = models.CharField(max_length=10)
      class Meta:
         #managed = False
        db_table = 'course_details'


#create your models here
class contact(models.Model):
      name = models.CharField(max_length=200)
      age  = models.IntegerField(default=0)
      email = models.EmailField()
      def __unicode__(self):
          return self.name

class tag(models.Model):
      contact = models.ForeignKey(contact)
      name = models.CharField(max_length=50)
      def __unicode__(self):
          return self.name


