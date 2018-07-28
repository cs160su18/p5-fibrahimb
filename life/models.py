from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField


class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
#company logs in
class User(models.Model):
  username = models.CharField(max_length = 150)
  password = models.CharField(max_length = 20)
  
class Send(models.Model):
  name = models.CharField(max_length=30)
  email = models.CharField(max_length = 50)
  phone = models.CharField(max_length = 20)
  date = models.DateField()
  time = models.TimeField()

  def __str__(self):
    return self.name
  
  @classmethod
  def create(cls, name, email, phone, date, time):
        created = cls(name=name, email=email, phone=phone, date=date, time=time)
        return created

class Jobs(models.Model):
  job_title = models.CharField(max_length = 50)
  description = models.CharField(max_length = 200)
  
  def __str__(self):
    return self.job_title
  
  @classmethod
  def create(cls, job_title, description):
        created = cls(job_title=job_title, description=description)
        return created